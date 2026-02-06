"""Get insights from DataFrames stored in dict and clean
it.

Imports
----------
import pandas

Functions
----------
-key_info(dfs: dict)
-clean_nan(dfs: dict) -> dict
-check_data(dfs: dict)
"""

import pandas as pd

def key_info(dfs: dict):
    """Print out df.info() for each DataFrame in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for key in dfs.keys():
        print()
        print(key)
        print(dfs[key].info())
        print(dfs[key].head(2))

def clean_nan_df(dfs: dict) -> dict:
    """Delete empty columns and duplicate rows
    in all DataFrames stored in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
        
    Returns
    ----------
    dict
        cleaned DataFrames as dict values
    """
    for name, df in dfs.items():
        dfs[name] = df.dropna(axis=1, how="all")
        
    return dfs

def deduplicate(dfs: dict) -> dict:
    """Delete duplicate rows in all DataFrames stored
    in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
        
    Returns
    ----------
    dict
        cleaned DataFrames as dict values
    """
    for name, df in dfs.items():
        dfs[name] = df.drop_duplicates(subset="id")
        
    return dfs

def check_data(dfs: dict):
    """Print number of unique values of each column for all
    DataFrames stored in dict.

    Prints notification if value is not a DataFrame.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for key, df in dfs.items():
        print()
        print(key)
        try:
            print(df.nunique())
        except:
            print('Lista')

#def clean_data(df, report=True):
    """Report = amount of deleted records, null,
    duplicates etc.
    """