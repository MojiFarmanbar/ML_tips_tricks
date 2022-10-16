import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def htb(data):
    """
    Applies the head/tail breaks algorithm to an array of data.
    Params
    ------
    data : list
        Array of data to apply ht-breaks
    Returns
    -------
    results : list 
        List of data representing break points
    """
    # test input
    assert data, "Input must not be empty."
    assert all(isinstance(datum, int) or isinstance(datum, float) for datum in data), "All input values must be numeric."

    results = []  # array of break points

    def htb_inner(data):
        """
        Inner ht breaks function for recursively computing the break points.
        """
        # Add mean to results
        data_length = float(len(data))
        data_mean = sum(data) / data_length
        results.append(data_mean)

        # Recursive call to get next break point
        head = [datum for datum in data if datum > data_mean]
        while len(head) > 1 and len(head) / data_length < 0.40:
            return htb_inner(head)

    htb_inner(data)

    return results

def head_tail_break_encode(dataframe: pd.DataFrame, col_names: list):
    """
    this function apply head/tail breaks on given dataframe and list of columns
    """

    i = 0
    for col in col_names:
        breaks = htb(list(dataframe[col]))
        digitized_values = np.digitize(dataframe[col], bins=breaks)
        digitized_values = digitized_values.reshape((-1,1))
        # one hot encoding
        enc = OneHotEncoder(sparse=False)
        ohe_values =  enc.fit_transform(digitized_values)
        # appending to the data
        if i == 0:
            one_hot_encoded = ohe_values
            i += 1
        else:
            one_hot_encoded = np.append(one_hot_encoded, ohe_values, axis=1) 
    return one_hot_encoded
