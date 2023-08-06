"""Plotting utilities."""
import os

from matplotlib import pyplot as plt


def plot_precision_recall_curve(params, results):
    """Plot precision-recall curve per category."""
    # Create output folder if not existing
    os.makedirs(params["folder_plot"], exist_ok=True)

    # Plot figures
    plt.figure(figsize=params["fig_size"])

    if params["data_n_output"] > 1:
        for label_cat in params["data_output_fields"]:
            plt.plot(
                results["rc_per_category"][label_cat],
                results["pr_per_category"][label_cat],
                ls="-",
            )

    plt.plot(
        results["rc_per_category"]["Overall"],
        results["pr_per_category"]["Overall"],
        ls="dashdot",
    )

    # Add title for pr_curve
    plt.title(
        f"P/R Curve of {params['project_name']}, average_precision_score: {results['mAp']:.4f}",
        fontsize=12,
        fontweight="bold",
    )
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend(results["mAp_per_category"].items())

    # Write to file
    plt.savefig(
        f"{params['folder_plot']}/{params['file_plot_pr']}",
        dpi=300,
        bbox_inches="tight",
    )

    plt.show()

    return


def plot_scatter(params, data, results):
    """Calculate MAE and scatter plots prediction against labels."""
    # Initialization
    os.makedirs(params["folder_plot"], exist_ok=True)
    if_str = "[IF]" if params["isolation"] else ""
    debug_str = "[Debug]" if params["debug_mode"] else ""

    plt.figure(figsize=params["fig_size"])

    for idx, field in enumerate(["", "_denormalized"]):
        # Calculate min-max values for equal axis
        mi = min(
            data[f"pred_val{field}"].values.min(),
            data[f"label_val{field}"].values.min(),
        )
        ma = max(
            data[f"pred_val{field}"].values.max(),
            data[f"label_val{field}"].values.max(),
        )

        plt.subplot(1, 2, idx + 1)
        plt.scatter(
            data[f"label_val{field}"],
            data[f"pred_val{field}"],
            s=3,
            alpha=0.3,
        )
        # Print equal line
        plt.plot([mi, ma], [mi, ma], c="tab:orange", linestyle="--")
        plt.xlabel(f"Real value {params['data_pred_unit']}")
        plt.ylabel(f"Predicted value {params['data_pred_unit']}")
        plt.title(
            f"{debug_str}{if_str} MAE per {params['project_name']}{field}: "
            f"{results[f'mae{field}']:.2f} {params['data_pred_unit']}"
        )

    # Save the plot
    plt.tight_layout()
    plt.savefig(
        f"{params['folder_plot']}/{params['session_id']}_{params['file_plot']}",
        dpi=300,
        bbox_inches="tight",
    )

    plt.show()

    return


def plot_distributions(params, data, col_info):
    """Plot data visualization."""
    # Create output folder if not existing
    os.makedirs(f"{params['folder_plot']}/{params['folder_plot_dist']}", exist_ok=True)

    # Initialize info
    col_name = col_info["name"]
    col_type = col_info["type"]
    data_points = data[col_name]
    na_rate = data_points.isna().sum() / data_points.shape[0]
    to_plot = False

    # Plot differently depending on data type
    if col_type == "numeric":

        # Drop NaNs
        data_points.dropna(inplace=True)

        # Count histogram bins
        hist_bins = min([len(data_points.unique()), 100])

        # Plot
        plt.figure(figsize=params["fig_size"])
        plt.hist(data[col_name], density=True, bins=hist_bins)
        to_plot = True

    elif col_type == "categorical":

        # Compute frequency table
        freq_table = data_points.value_counts(dropna=False, normalize=True).loc[
            lambda x: x > 1e-3
        ]

        # Plot
        freq_table.plot(kind="bar", figsize=params["fig_size"])
        to_plot = True

    # Decorate plots
    if to_plot:
        plt.grid()
        plt.xlabel(f"{col_name} values")
        plt.ylabel("Distribution")
        plt.title(f"Distribution of {col_name} - NA rate = {100 * na_rate:.2f} %")

        label = "train" if params["train_mode"] else "test"

        # Write to file
        plt.savefig(
            f"{params['folder_plot']}/{params['folder_plot_dist']}/{label}_{col_name}",
            dpi=300,
            bbox_inches="tight",
        )

        plt.show()

    return


def plot_model_results(params, data, results):
    """Plot model results."""
    if params["prediction_type"] == "classification":
        # Plot P/R curves per category
        plot_precision_recall_curve(params, results)
        plot_kappa_analysis(params, results)
        plot_lift_curve(params, results)

    elif params["prediction_type"] == "regression":
        plot_scatter(params, data, results)

    else:
        raise ValueError(
            "Prediction_type should either be 'classification' or 'regression'"
        )


def plot_kappa_analysis(params, results):
    """Plot kappa analysis by kappa scatter plot and kappa histogram."""
    # Histogram of predictions
    plt.figure(figsize=(8, 5))
    plt.hist(results["pr"], bins=30, log=True)
    plt.title("Histogram of Prediction values")
    plt.xlabel("Prediction")
    plt.ylabel("Count")
    plt.tight_layout()

    # Save the plot
    plt.savefig(
        f"{params['folder_plot']}/pred_hist.png",
        dpi=300,
        bbox_inches="tight",
    )

    # Scatter plot of Kappa values
    plt.figure(figsize=(8, 5))
    plt.scatter(results["x"], results["k"], s=3)
    plt.title(f"Kappa values over thresholds. Best threshold: {results['best_x']}")
    plt.xlabel("Threshold")
    plt.ylabel("Kappa value")
    plt.tight_layout()

    # Save the plot
    plt.savefig(
        f"{params['folder_plot']}/kappa_plot.png",
        dpi=300,
        bbox_inches="tight",
    )


def plot_lift_curve(params, results):
    """Plot lift curve of training and validation for all categories."""
    for i in range(params["data_n_output"]):
        plt.figure()
        # Plot the figure
        x, y_train = results["lift_train"][i]
        _, y_val = results["lift_val"][i]

        plt.plot(x, y_train)
        plt.plot(x, y_val)

        segments = ["train", "val"]
        if "validation_test_split" in params and params["validation_test_split"]:
            _, y_test = results["lift_test"][i]
            plt.plot(x, y_test)
            segments = ["train", "val", "test"]

        plt.ylabel("Lift")
        plt.xlabel("Percentile")
        plt.title(f'Lift Curve: {params["data_output_fields"][i]}')
        plt.legend(segments)

        # Save the plot
        plt.savefig(
            f"{params['folder_plot']}/lift_{params['data_output_fields'][i]}.png",
            dpi=300,
            bbox_inches="tight",
        )

        plt.show()
