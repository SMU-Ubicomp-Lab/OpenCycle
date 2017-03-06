import numpy as np
import seaborn as sns

def modified_bland_altman_plot(predicted, truth):
    """Plot residuals of the given predictions.

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
    truth = np.asarray(truth, dtype=np.int)
    diff = predicted - truth

    ax = sns.stripplot(truth, diff, jitter=True)
    ax.set(xlabel='truth', ylabel='difference from truth', title="Modified Bland-Altman Plot")

    # Plot a horizontal line at 0
    ax.axhline(0, ls=":", c=".2")

    return ax

