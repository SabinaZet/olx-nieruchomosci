"""Store data in CSV, SQL and Parquet formats.

Imports
----------
import pandas

Functions
----------
-save_csv(dfs: dict, cols: list)
-save_sql(dfs: dict, cols: list)
-save_parquet(dfs: dict, cols: list)
"""
import pandas as pd

cols = [
        'data_location', 'data_timing', 'data_category',
        'data_business', 'data_offer', 'data_promoted'
        ]

def save_csv(dfs: dict, cols: list = cols):
    """Save DataFrames to CSV files in projects data directory.

    Parameters
    ----------
    dfs : dict
        DataFrames as values
    cols : list
        DataFrames to save
    """
    f = pd.Timestamp.now('Europe/Warsaw').strftime("%d.%m.%Y")
    for col in cols:
        name = f"/home/itsme/Projekty/olx-nieruchomosci/data/csv/{col + ' ' + str(f)}.csv"
        if col not in dfs:
            continue
        
        dfs[col].to_csv(name)
        
#def save_sql(dfs: dict, cols: list):
    """Save DataFrames to SQL files in projects data directory.

    Parameters
    ----------
    dfs : dict
        DataFrames as values
    cols : list
        DataFrames to save
    """
    
#def save_parquet(dfs: dict, cols: list):
    """Save DataFrames to Parquet files in projects
    data directory.

    Parameters
    ----------
    dfs : dict
        DataFrames as values
    cols : list
        DataFrames to save
    """