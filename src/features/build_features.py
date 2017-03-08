import pandas as pd

BY_ID = ['ID']
BY_GROUP = ['ID', 'GROUP_ID']
BY_CYCLE = ['ID', 'GROUP_ID', 'CYCLE_ID']


def previous_value(x, df, grouping=BY_GROUP, window_size=1):
    """Determine mean of previous n measurements for a participant.

    Parameters
    ----------
    x : str
        The name of the column whose history we consider.
    df : pd.DataFrame
        The relevant data frame.
    grouping : list
        Any relevant stratification of the data.
    window_size : int
        The number of records backward to look.

    Returns
    -------
    The mean of the past $n$ measurements for a particular grouping level.
    """
    return df.groupby(grouping)[x].shift(1).rolling(window_size).mean()
