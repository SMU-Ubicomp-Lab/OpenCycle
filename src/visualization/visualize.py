import numpy as np
import matplotlib.pyplot as plt


def _generic_residual_plot(x, y, title="", xaxis="", hue=None):
    if hue is None:
        hue = x
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=9, c=hue, cmap="winter")
    ax.set_xlabel(xaxis)
    ax.set_ylabel('difference from truth')
    ax.set_title("Modified Bland-Altman Plot")

    # Plot a horizontal line at 0
    ax.axhline(0, ls=":", c=".2")

    return ax


def modified_bland_altman_plot(predicted, truth):
    """Plot residuals of the given predictions against truth.

    Parameters
    ----------
    predicted : array-like, shape (n, )
        The predicted values.

    truth : array-like, shape (n, )
        The true values.

    Returns
    -------
    ax : matplotlib axis
        The axis on which the plot was made.

    """
    predicted = np.asarray(predicted)
    truth = np.asarray(truth)
    diff = truth - predicted  # stats.stackoverflow told me to.

    return _generic_residual_plot(truth, diff,
                                  title="Modified Bland-Altman Plot",
                                  xaxis="truth",
                                  hue=predicted)


def residual_plot(predicted, truth):
    """Plot residuals of the given predictions against predicted (fitted) values.

    Parameters
    ----------
    predicted : array-like, shape (n, )
        The predicted values.

    truth : array-like, shape (n, )
        The true values.

    Returns
    -------
    ax : matplotlib axis
        The axis on which the plot was made.

    """
    predicted = np.asarray(predicted)
    truth = np.asarray(truth)
    diff = truth - predicted  # stats.stackoverflow told me to.

    return _generic_residual_plot(predicted, diff,
                                  title="Residuals",
                                  xaxis="predicted",
                                  hue=truth)
