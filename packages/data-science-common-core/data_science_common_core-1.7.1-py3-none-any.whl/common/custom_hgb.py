"""Custom made HGB classifier that takes validation data on fit."""
import warnings
from abc import ABC
from timeit import default_timer as time

import numpy as np
from sklearn._loss import HalfBinomialLoss
from sklearn._loss.loss import BaseLoss, HalfMultinomialLoss
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble._hist_gradient_boosting._gradient_boosting import (
    _update_raw_predictions,
)
from sklearn.ensemble._hist_gradient_boosting.binning import _BinMapper
from sklearn.ensemble._hist_gradient_boosting.common import G_H_DTYPE, X_DTYPE, Y_DTYPE
from sklearn.ensemble._hist_gradient_boosting.gradient_boosting import (
    BaseHistGradientBoosting,
    _update_leaves_values,
)
from sklearn.ensemble._hist_gradient_boosting.grower import TreeGrower
from sklearn.metrics import check_scoring
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import check_random_state
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import _check_sample_weight, check_consistent_length


class CustomBaseHistGradientBoosting(BaseHistGradientBoosting, BaseEstimator, ABC):
    """Custom HGB class, you have no idea.."""

    def fit(self, X, y, eval_set=None, sample_weight=None):
        """Fit the gradient boosting model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.
        y : array-like of shape (n_samples,)
            Target values.
        sample_weight : array-like of shape (n_samples,) default=None
            Weights of training data.
            .. versionadded:: 0.23
        Returns
        -------
        self : object
            Fitted estimator.
        """
        fit_start_time = time()
        acc_find_split_time = 0.0  # time spent finding the best splits
        acc_apply_split_time = 0.0  # time spent splitting nodes
        acc_compute_hist_time = 0.0  # time spent computing histograms
        # time spent predicting X for gradient and hessians update
        acc_prediction_time = 0.0
        X, y = self._validate_data(X, y, dtype=[X_DTYPE], force_all_finite=False)
        y = self._encode_y(y)
        X_valid, y_valid = eval_set
        X_valid, y_valid = self._validate_data(
            X_valid, y_valid, dtype=[X_DTYPE], force_all_finite=False
        )
        y_valid = self._encode_y(y_valid)
        check_consistent_length(X, y)
        check_consistent_length(X_valid, y_valid)
        # Do not create unit sample weights by default to later skip some
        # computation
        if sample_weight is not None:
            sample_weight = _check_sample_weight(sample_weight, X, dtype=np.float64)
            # TODO: remove when PDP supports sample weights
            self._fitted_with_sw = True

        rng = check_random_state(self.random_state)

        # When warm starting, we want to re-use the same seed that was used
        # the first time fit was called (e.g. for subsampling or for the
        # train/val split).
        if not (self.warm_start and self._is_fitted()):
            self._random_seed = rng.randint(np.iinfo(np.uint32).max, dtype="u8")

        self._validate_parameters()

        # used for validation in predict
        n_samples, self._n_features = X.shape

        self.is_categorical_, known_categories = self._check_categories(X)

        # we need this stateful variable to tell raw_predict() that it was
        # called from fit() (this current method), and that the data it has
        # received is pre-binned.
        # predicting is faster on pre-binned data, so we want early stopping
        # predictions to be made on pre-binned data. Unfortunately the _scorer
        # can only call predict() or predict_proba(), not raw_predict(), and
        # there's no way to tell the scorer that it needs to predict binned
        # data.
        self._in_fit = True

        # `_openmp_effective_n_threads` is used to take cgroups CPU quotes
        # into account when determine the maximum number of threads to use.
        n_threads = _openmp_effective_n_threads()

        if isinstance(self.loss, str):
            self._loss = self._get_loss(sample_weight=sample_weight)
        elif isinstance(self.loss, BaseLoss):
            self._loss = self.loss

        if self.early_stopping == "auto":
            self.do_early_stopping_ = n_samples > 10000
        else:
            self.do_early_stopping_ = self.early_stopping

        # create validation data if needed
        self._use_validation_data = self.validation_fraction is not None
        if self.do_early_stopping_ and self._use_validation_data:
            # stratify for classification
            # instead of checking predict_proba, loss.n_classes >= 2 would also work
            stratify = y if hasattr(self._loss, "predict_proba") else None

            # Save the state of the RNG for the training and validation split.
            # This is needed in order to have the same split when using
            # warm starting.

            if sample_weight is None:
                if X_valid is None:
                    X_train, X_val, y_train, y_val = train_test_split(
                        X,
                        y,
                        test_size=self.validation_fraction,
                        stratify=stratify,
                        random_state=self._random_seed,
                    )
                    sample_weight = sample_weight = None

                else:
                    X_train, X_val, y_train, y_val = X, X_valid, y, y_valid
            else:
                # TODO: incorporate sample_weight in sampling here, as well as
                # stratify
                (
                    X_train,
                    X_val,
                    y_train,
                    y_val,
                    sample_weight,
                    sample_weight,
                ) = train_test_split(
                    X,
                    y,
                    sample_weight,
                    test_size=self.validation_fraction,
                    stratify=stratify,
                    random_state=self._random_seed,
                )
        else:
            X_train, y_train, sample_weight = X, y, sample_weight
            X_val = y_val = sample_weight = None

        # Bin the data
        # For ease of use of the API, the user-facing GBDT classes accept the
        # parameter max_bins, which doesn't take into account the bin for
        # missing values (which is always allocated). However, since max_bins
        # isn't the true maximal number of bins, all other private classes
        # (binmapper, histbuilder...) accept n_bins instead, which is the
        # actual total number of bins. Everywhere in the code, the
        # convention is that n_bins == max_bins + 1
        n_bins = self.max_bins + 1  # + 1 for missing values
        self._bin_mapper = _BinMapper(
            n_bins=n_bins,
            is_categorical=self.is_categorical_,
            known_categories=known_categories,
            random_state=self._random_seed,
            n_threads=n_threads,
        )
        X_binned_train = self._bin_data(X_train, is_training_data=True)
        if X_val is not None:
            X_binned_val = self._bin_data(X_val, is_training_data=False)
        else:
            X_binned_val = None

        # Uses binned data to check for missing values
        has_missing_values = (
            (X_binned_train == self._bin_mapper.missing_values_bin_idx_)
            .any(axis=0)
            .astype(np.uint8)
        )

        if self.verbose:
            print("Fitting gradient boosted rounds:")

        n_samples = X_binned_train.shape[0]

        # First time calling fit, or no warm start
        if not (self._is_fitted() and self.warm_start):
            # Clear random state and score attributes
            self._clear_state()

            # initialize raw_predictions: those are the accumulated values
            # predicted by the trees for the training data. raw_predictions has
            # shape (n_samples, n_trees_per_iteration) where
            # n_trees_per_iterations is n_classes in multiclass classification,
            # else 1.
            # self._baseline_prediction has shape (1, n_trees_per_iteration)
            self._baseline_prediction = self._loss.fit_intercept_only(
                y_true=y_train, sample_weight=sample_weight
            ).reshape((1, -1))
            raw_predictions = np.zeros(
                shape=(n_samples, self.n_trees_per_iteration_),
                dtype=self._baseline_prediction.dtype,
                order="F",
            )
            raw_predictions += self._baseline_prediction

            # predictors is a matrix (list of lists) of TreePredictor objects
            # with shape (n_iter_, n_trees_per_iteration)
            self._predictors = predictors = []

            # Initialize structures and attributes related to early stopping
            self._scorer = None  # set if scoring != loss
            raw_predictions_val = None  # set if scoring == loss and use val
            self.train_score_ = []
            self.validation_score_ = []

            if self.do_early_stopping_:
                # populate train_score and validation_score with the
                # predictions of the initial model (before the first tree)

                if self.scoring == "loss":
                    # we're going to compute scoring w.r.t the loss. As losses
                    # take raw predictions as input (unlike the scorers), we
                    # can optimize a bit and avoid repeating computing the
                    # predictions of the previous trees. We'll re-use
                    # raw_predictions (as it's needed for training anyway) for
                    # evaluating the training loss, and create
                    # raw_predictions_val for storing the raw predictions of
                    # the validation data.

                    if self._use_validation_data:
                        raw_predictions_val = np.zeros(
                            shape=(X_binned_val.shape[0], self.n_trees_per_iteration_),
                            dtype=self._baseline_prediction.dtype,
                            order="F",
                        )

                        raw_predictions_val += self._baseline_prediction

                    self._check_early_stopping_loss(
                        raw_predictions=raw_predictions,
                        y_train=y_train,
                        sample_weight_train=sample_weight,
                        raw_predictions_val=raw_predictions_val,
                        y_val=y_val,
                        sample_weight_val=sample_weight,
                        n_threads=n_threads,
                    )
                else:
                    self._scorer = check_scoring(self, self.scoring)
                    # _scorer is a callable with signature (est, X, y) and
                    # calls est.predict() or est.predict_proba() depending on
                    # its nature.
                    # Unfortunately, each call to _scorer() will compute
                    # the predictions of all the trees. So we use a subset of
                    # the training set to compute train scores.

                    # Compute the subsample set
                    (
                        X_binned_small_train,
                        y_small_train,
                        sample_weight_small_train,
                    ) = self._get_small_trainset(
                        X_binned_train, y_train, sample_weight, self._random_seed
                    )

                    self._check_early_stopping_scorer(
                        X_binned_small_train,
                        y_small_train,
                        sample_weight_small_train,
                        X_binned_val,
                        y_val,
                        sample_weight,
                    )
            begin_at_stage = 0

        # warm start: this is not the first time fit was called
        else:
            # Check that the maximum number of iterations is not smaller
            # than the number of iterations from the previous fit
            if self.max_iter < self.n_iter_:
                raise ValueError(
                    "max_iter=%d must be larger than or equal to "
                    "n_iter_=%d when warm_start==True" % (self.max_iter, self.n_iter_)
                )

            # Convert array attributes to lists
            self.train_score_ = self.train_score_.tolist()
            self.validation_score_ = self.validation_score_.tolist()

            # Compute raw predictions
            raw_predictions = self._raw_predict(X_binned_train, n_threads=n_threads)
            if self.do_early_stopping_ and self._use_validation_data:
                raw_predictions_val = self._raw_predict(
                    X_binned_val, n_threads=n_threads
                )
            else:
                raw_predictions_val = None

            if self.do_early_stopping_ and self.scoring != "loss":
                # Compute the subsample set
                (
                    X_binned_small_train,
                    y_small_train,
                    sample_weight_small_train,
                ) = self._get_small_trainset(
                    X_binned_train, y_train, sample_weight, self._random_seed
                )

            # Get the predictors from the previous fit
            predictors = self._predictors

            begin_at_stage = self.n_iter_

        # initialize gradients and hessians (empty arrays).
        # shape = (n_samples, n_trees_per_iteration).
        gradient, hessian = self._loss.init_gradient_and_hessian(
            n_samples=n_samples, dtype=G_H_DTYPE, order="F"
        )

        for iteration in range(begin_at_stage, self.max_iter):

            if self.verbose:
                iteration_start_time = time()
                print(
                    "[{}/{}] ".format(iteration + 1, self.max_iter), end="", flush=True
                )

            # Update gradients and hessians, inplace
            # Note that self._loss expects shape (n_samples,) for
            # n_trees_per_iteration = 1 else shape (n_samples, n_trees_per_iteration).
            if self._loss.constant_hessian:
                self._loss.gradient(
                    y_true=y_train,
                    raw_prediction=raw_predictions,
                    sample_weight=sample_weight,
                    gradient_out=gradient,
                    n_threads=n_threads,
                )
            else:
                self._loss.gradient_hessian(
                    y_true=y_train,
                    raw_prediction=raw_predictions,
                    sample_weight=sample_weight,
                    gradient_out=gradient,
                    hessian_out=hessian,
                    n_threads=n_threads,
                )

            # Append a list since there may be more than 1 predictor per iter
            predictors.append([])

            # 2-d views of shape (n_samples, n_trees_per_iteration_) or (n_samples, 1)
            # on gradient and hessian to simplify the loop over n_trees_per_iteration_.
            if gradient.ndim == 1:
                g_view = gradient.reshape((-1, 1))
                h_view = hessian.reshape((-1, 1))
            else:
                g_view = gradient
                h_view = hessian

            # Build `n_trees_per_iteration` trees.
            for k in range(self.n_trees_per_iteration_):
                grower = TreeGrower(
                    X_binned=X_binned_train,
                    gradients=g_view[:, k],
                    hessians=h_view[:, k],
                    n_bins=n_bins,
                    n_bins_non_missing=self._bin_mapper.n_bins_non_missing_,
                    has_missing_values=has_missing_values,
                    is_categorical=self.is_categorical_,
                    monotonic_cst=self.monotonic_cst,
                    max_leaf_nodes=self.max_leaf_nodes,
                    max_depth=self.max_depth,
                    min_samples_leaf=self.min_samples_leaf,
                    l2_regularization=self.l2_regularization,
                    shrinkage=self.learning_rate,
                    n_threads=n_threads,
                )
                grower.grow()

                acc_apply_split_time += grower.total_apply_split_time
                acc_find_split_time += grower.total_find_split_time
                acc_compute_hist_time += grower.total_compute_hist_time

                if self._loss.need_update_leaves_values:
                    _update_leaves_values(
                        loss=self._loss,
                        grower=grower,
                        y_true=y_train,
                        raw_prediction=raw_predictions[:, k],
                        sample_weight=sample_weight,
                    )

                predictor = grower.make_predictor(
                    binning_thresholds=self._bin_mapper.bin_thresholds_
                )
                predictors[-1].append(predictor)

                # Update raw_predictions with the predictions of the newly
                # created tree.
                tic_pred = time()
                _update_raw_predictions(raw_predictions[:, k], grower, n_threads)
                toc_pred = time()
                acc_prediction_time += toc_pred - tic_pred

            should_early_stop = False
            if self.do_early_stopping_:
                if self.scoring == "loss":
                    # Update raw_predictions_val with the newest tree(s)
                    if self._use_validation_data:
                        for k, pred in enumerate(self._predictors[-1]):
                            raw_predictions_val[:, k] += pred.predict_binned(
                                X_binned_val,
                                self._bin_mapper.missing_values_bin_idx_,
                                n_threads,
                            )

                    should_early_stop = self._check_early_stopping_loss(
                        raw_predictions=raw_predictions,
                        y_train=y_train,
                        sample_weight_train=sample_weight,
                        raw_predictions_val=raw_predictions_val,
                        y_val=y_val,
                        sample_weight_val=sample_weight,
                        n_threads=n_threads,
                    )

                else:
                    should_early_stop = self._check_early_stopping_scorer(
                        X_binned_small_train,
                        y_small_train,
                        sample_weight_small_train,
                        X_binned_val,
                        y_val,
                        sample_weight,
                    )

            if self.verbose:
                self._print_iteration_stats(iteration_start_time)

            # maybe we could also early stop if all the trees are stumps?
            if should_early_stop:
                break

        if self.verbose:
            duration = time() - fit_start_time
            n_total_leaves = sum(
                predictor.get_n_leaf_nodes()
                for predictors_at_ith_iteration in self._predictors
                for predictor in predictors_at_ith_iteration
            )
            n_predictors = sum(
                len(predictors_at_ith_iteration)
                for predictors_at_ith_iteration in self._predictors
            )
            print(
                "Fit {} trees in {:.3f} s, ({} total leaves)".format(
                    n_predictors, duration, n_total_leaves
                )
            )
            print(
                "{:<32} {:.3f}s".format(
                    "Time spent computing histograms:", acc_compute_hist_time
                )
            )
            print(
                "{:<32} {:.3f}s".format(
                    "Time spent finding best splits:", acc_find_split_time
                )
            )
            print(
                "{:<32} {:.3f}s".format(
                    "Time spent applying splits:", acc_apply_split_time
                )
            )
            print(
                "{:<32} {:.3f}s".format("Time spent predicting:", acc_prediction_time)
            )

        self.train_score_ = np.asarray(self.train_score_)
        self.validation_score_ = np.asarray(self.validation_score_)
        del self._in_fit  # hard delete so we're sure it can't be used anymore
        return self


class CustomHistGradientBoostingClassifier(
    ClassifierMixin, CustomBaseHistGradientBoosting
):
    """Class definition stub."""

    _VALID_LOSSES = (
        "log_loss",
        "binary_crossentropy",
        "categorical_crossentropy",
        "auto",
    )

    def __init__(
        self,
        loss="log_loss",
        *,
        learning_rate=0.1,
        max_iter=100,
        max_leaf_nodes=31,
        max_depth=None,
        min_samples_leaf=20,
        l2_regularization=0.0,
        max_bins=255,
        categorical_features=None,
        monotonic_cst=None,
        warm_start=False,
        early_stopping="auto",
        scoring="loss",
        validation_fraction=0.1,
        n_iter_no_change=10,
        tol=1e-7,
        verbose=0,
        random_state=None,
    ):
        """Init, just filling for pre-commit."""
        super().__init__(
            loss=loss,
            learning_rate=learning_rate,
            max_iter=max_iter,
            max_leaf_nodes=max_leaf_nodes,
            max_depth=max_depth,
            min_samples_leaf=min_samples_leaf,
            l2_regularization=l2_regularization,
            max_bins=max_bins,
            categorical_features=categorical_features,
            monotonic_cst=monotonic_cst,
            warm_start=warm_start,
            early_stopping=early_stopping,
            scoring=scoring,
            validation_fraction=validation_fraction,
            n_iter_no_change=n_iter_no_change,
            tol=tol,
            verbose=verbose,
            random_state=random_state,
        )

    def _encode_y(self, y):
        """Of course nothing would be complete without encode."""
        # encode classes into 0 ... n_classes - 1 and sets attributes classes_
        # and n_trees_per_iteration_
        check_classification_targets(y)

        label_encoder = LabelEncoder()
        encoded_y = label_encoder.fit_transform(y)
        self.classes_ = label_encoder.classes_
        n_classes = self.classes_.shape[0]
        # only 1 tree for binary classification. For multiclass classification,
        # we build 1 tree per class.
        self.n_trees_per_iteration_ = 1 if n_classes <= 2 else n_classes
        encoded_y = encoded_y.astype(Y_DTYPE, copy=False)
        return encoded_y

    def _get_loss(self, sample_weight):
        """Get your loss."""
        # TODO(1.3): Remove "auto", "binary_crossentropy", "categorical_crossentropy"
        if self.loss in ("auto", "binary_crossentropy", "categorical_crossentropy"):
            warnings.warn(
                f"The loss '{self.loss}' was deprecated in v1.1 and will be removed in "
                "version 1.3. Use 'log_loss' which is equivalent.",
                FutureWarning,
            )

        if self.loss in ("log_loss", "auto"):
            if self.n_trees_per_iteration_ == 1:
                return HalfBinomialLoss(sample_weight=sample_weight)
            else:
                return HalfMultinomialLoss(
                    sample_weight=sample_weight, n_classes=self.n_trees_per_iteration_
                )
        if self.loss == "categorical_crossentropy":
            if self.n_trees_per_iteration_ == 1:
                raise ValueError(
                    f"loss='{self.loss}' is not suitable for a binary classification "
                    "problem. Please use loss='log_loss' instead."
                )
            else:
                return HalfMultinomialLoss(
                    sample_weight=sample_weight, n_classes=self.n_trees_per_iteration_
                )
        if self.loss == "binary_crossentropy":
            if self.n_trees_per_iteration_ > 1:
                raise ValueError(
                    f"loss='{self.loss}' is not defined for multiclass "
                    f"classification with n_classes={self.n_trees_per_iteration_}, "
                    "use loss='log_loss' instead."
                )
            else:
                return HalfBinomialLoss(sample_weight=sample_weight)

    def predict(self, X):
        """Predict classes for X.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.
        Returns
        -------
        y : ndarray, shape (n_samples,)
            The predicted classes.
        """
        # TODO: This could be done in parallel
        encoded_classes = np.argmax(self.predict_proba(X), axis=1)
        return self.classes_[encoded_classes]

    def staged_predict(self, X):
        """Predict classes at each iteration.

        This method allows monitoring (i.e. determine error on testing set)
        after each stage.
        .. versionadded:: 0.24
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.
        Yields
        ------
        y : generator of ndarray of shape (n_samples,)
            The predicted classes of the input samples, for each iteration.
        """
        for proba in self.staged_predict_proba(X):
            encoded_classes = np.argmax(proba, axis=1)
            yield self.classes_.take(encoded_classes, axis=0)

    def predict_proba(self, X):
        """Predict class probabilities for X.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.
        Returns
        -------
        p : ndarray, shape (n_samples, n_classes)
            The class probabilities of the input samples.
        """
        raw_predictions = self._raw_predict(X)
        return self._loss.predict_proba(raw_predictions)

    def staged_predict_proba(self, X):
        """Predict class probabilities at each iteration.

        This method allows monitoring (i.e. determine error on testing set)
        after each stage.
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.
        Yields
        ------
        y : generator of ndarray of shape (n_samples,)
            The predicted class probabilities of the input samples,
            for each iteration.
        """
        for raw_predictions in self._staged_raw_predict(X):
            yield self._loss.predict_proba(raw_predictions)

    def decision_function(self, X):
        """Compute the decision function of ``X``.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.
        Returns
        -------
        decision : ndarray, shape (n_samples,) or \
                (n_samples, n_trees_per_iteration)
            The raw predicted values (i.e. the sum of the trees leaves) for
            each sample. n_trees_per_iteration is equal to the number of
            classes in multiclass classification.
        """
        decision = self._raw_predict(X)
        if decision.shape[1] == 1:
            decision = decision.ravel()
        return decision

    def staged_decision_function(self, X):
        """Compute decision function of ``X`` for each iteration.

        This method allows monitoring (i.e. determine error on testing set)
        after each stage.
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.
        Yields
        ------
        decision : generator of ndarray of shape (n_samples,) or \
                (n_samples, n_trees_per_iteration)
            The decision function of the input samples, which corresponds to
            the raw values predicted from the trees of the ensemble . The
            classes corresponds to that in the attribute :term:`classes_`.
        """
        for staged_decision in self._staged_raw_predict(X):
            if staged_decision.shape[1] == 1:
                staged_decision = staged_decision.ravel()
            yield staged_decision
