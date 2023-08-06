"""Pipeline functions and Transformers."""

from sklearn.pipeline import Pipeline


class PipelineExtended(Pipeline):
    """Parametrized transformer that takes run time parameters."""

    def transform(self, X, **fit_params):
        """Transform function.

        Fit params should include the name of the transformation and then __ then variable name
        Example:
            Suppose you have a transformer called 'numerical' which takes a parameter called 'index'
            Then you fit the pipeline as:
            p = PipelineExtended(...)
            p.fit(X,fit_params = {'numerical__index':...})
            p.transform(X,fit_params = {'numerical__index':...})
        """
        fit_params_steps = self._check_fit_params(**fit_params)
        Xt = X
        for (_, _, transform), (k, v) in zip(self._iter(), fit_params_steps.items()):
            if len(v) > 0:
                Xt = transform.transform(Xt, **v)
            else:
                Xt = transform.transform(Xt)
        return Xt
