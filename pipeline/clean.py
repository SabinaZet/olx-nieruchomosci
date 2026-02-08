"""Get insights from DataFrames stored in dict and clean
it.

Imports
----------
import pandas
from pandas.api.types import is_datetime64_any_dtype,
    is_object_dtype, is_bool_dtype, is_numeric_dtype

Functions
----------
-key_info(dfs: dict)
-clean_nan(dfs: dict)
-deduplicate(dfs: dict)
-check_data(dfs: dict)
-nan_report(dfs: dict, report: bool) -> dict
-delete_columns(dfs: dict, DEL_MAP: dict)
-id_index(dfs: dict)
-col_names(dfs: dict)
-clean_url(dfs: dict)
-change_dtypes(dfs: dict, DTYPE_MAP: dict)
-clean_data(dfs: dict) -> dict
"""

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_object_dtype, is_bool_dtype, is_numeric_dtype

DEL_MAP = {
    'data_location' : 'map.zoom',
    'data_category' : 'offer_type',
    'data_business' : ['user.is_online','contact.courier'],
    'data_offer' : [
        'location.city.id', 'location.city._nodeId', 'location.city.normalized_name', 'location.district.id', 'location.district._nodeId', 
        'location.region.id', 'location.region.normalized_name', 'location.region._nodeId'
        ]
}

DTYPE_MAP = {
    'data_location' : {
        'isGpsrAvailable' : 'bool',
        'city id' : 'object',
        'city name' : 'object',
        'city normalized_name' : 'object',
        'city _nodeId' : 'object',
        'region id' : 'object',
        'region name' : 'object',
        'region normalized_name' : 'object',
        'region _nodeId' : 'object',
        'map lat' : 'float',
        'map lon' : 'float',
        'map radius' : 'int',
        'map show_detailed' : 'bool',
        'district id' : 'object',
        'district name' : 'object',
        'district _nodeId' : 'object'
    },
    'data_timing' : {
        'last refresh time' : 'datetime',
        'created time' : 'datetime',
        'omnibus pushup time' : 'datetime',
        'valid to time' : 'datetime'
    },
    'data_category' : {
        'category id' : 'category',
        'type' : 'category',
        '_nodeId' : 'object'
    },
    'data_business' : {
        'business' : 'bool',
        'protect_phone' : 'bool',
        'contact chat' : 'bool',
        'contact name' : 'object',
        'contact negotiation' : 'bool',
        'contact phone' : 'bool',
        'shop subdomain' : 'object',
        'user id' : 'object',
        'user uuid' : 'object',
        'user _nodeId' : 'object',
        'user about' : 'object',
        'user b2c_business_page' : 'bool',
        'user banner_desktop' : 'object',
        'user banner_mobile' : 'object',
        'user company_name' : 'object',
        'user created' : 'datetime',
        'user last_seen' : 'datetime',
        'user logo_ad_page' : 'object',
        'user name' : 'object',
        'user other_ads_enabled' : 'bool',
        'user photo' : 'object',
        'user social_network_account_type' : 'category',
        'user verification status' : 'object',
        'partner code' : 'object'
    },
    'data_offer' : {
        '_nodeId' : 'object',
        'title' : 'object',
        'status' : 'category',
        'url' : 'object',
        'description' : 'object',
        'external_url' : 'object',
        'city name' : 'object',
        'region name' :'object',
        'district name' : 'object'

    },
    'data_promoted' : {
        'highlighted' : 'bool',
        'top_ad' : 'bool',
        'options' : 'object',
        'premium_ad_page' : 'bool',
        'urgent' : 'bool',
        'b2c_ad_page' : 'bool'
    }
}

def key_info(dfs: dict):
    """Print out df.info(), nunique() and head[2] for
    each DataFrame in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for key in dfs.keys():
        print()
        print(key)
        print(dfs[key].info())
        print()
        print('Unique values in columns:')
        
        try:
            print(dfs[key].nunique())
        except:
            print('Lista')
            
        print(dfs[key].head(2))

def clean_nan(dfs: dict):
    """Delete empty columns in all DataFrames stored
    in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for name, df in dfs.items():
        dfs[name] = df.dropna(axis=1, how="all")
        
def clean_url(dfs: dict):
    """Delete rows in data_offer where there is no url.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    dfs['data_offer'].dropna(subset='url', inplace=True)

def deduplicate(dfs: dict):
    """Delete duplicate rows in all DataFrames stored
    in dict.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for name, df in dfs.items():
        dfs[name] = df.drop_duplicates(subset="id")

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

def nan_report(dfs: dict, report: bool = True) -> dict:
    """Report = amount of deleted records, null,
    duplicates etc returned as dict.
    
    Parameters
    ----------
    dfs : dict
        DataFrames as values
    report : bool
        prints out the report, default: True
        
    Returns
    ----------
    dict
        categories as keys and report as values
    """
    nan_vals = {name: df.isna().sum()
                for name, df in dfs.items()}
    if report == True:
        for n, d in nan_vals.items():
            print(f'\nNumber of NaN values in columns of {n}:')
            print(d)
            
    return nan_vals

def delete_columns(dfs: dict, DEL_MAP: dict = DEL_MAP):
    """Delete columns that aren't needed.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    MAP : dict
        DataFrame names as keys and column names
        to delete as values
    """
    for name, col in DEL_MAP.items():
        dfs[name].drop(col, inplace=True, axis=1)
        
def id_index(dfs: dict):
    """Set indexes for DataFrames to 'id' values.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    for name, col in dfs.items():
        dfs[name] = dfs[name].set_index('id')
        
def col_names(dfs: dict):
    """Change column names in DataFrames.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    """
    COL_MAP = {
        'data_location' : {
            name : name.strip().replace('location.', '').replace('.', ' ')
            if 'location.' in name else
            name.strip().replace('.', ' ')
            for name in dfs['data_location'].columns
        },
        'data_timing' : {
            name : name.strip().replace('_', ' ')
            for name in dfs['data_timing'].columns},
        'data_category' : {
            name : name.strip().replace('category.', '')
            if '.id' not in name else
            name.strip().replace('.', ' ')
            for name in dfs['data_category']
        },
        'data_business' : {
            name : name.strip().replace('.', ' ')
            for name in dfs['data_business'].columns},
        'data_offer' : {
            name : name.strip().replace('location.', '').replace('.', ' ')
            for name in dfs['data_offer'].columns},
        'data_promoted' : {
            name : name.strip().replace('promotion.', '')
            for name in dfs['data_promoted'].columns}
    }
            
    for name, col in COL_MAP.items():
        dfs[name].rename(columns=col, inplace=True)

def change_dtypes(dfs: dict, DTYPE_MAP: dict=DTYPE_MAP):
    """Change column dtypes in DataFrames using
    dict type DTYPE_MAP.

    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
    DTYPE_MAP : dict
        DataFrame names as keys and column dtypes
        as values
    """
    for name, df in DTYPE_MAP.items():
        if name not in dfs:
            continue

        for col_name, dtype in df.items():
            if col_name not in dfs[name].columns:
                continue

            if dtype == 'datetime' and not is_datetime64_any_dtype(dfs[name][col_name]):
                dfs[name][col_name] = pd.to_datetime(dfs[name][col_name], utc=True, errors="coerce").dt.tz_convert('Europe/Warsaw')

            elif dtype == 'object' and not is_object_dtype(dfs[name][col_name]):
                dfs[name][col_name] = dfs[name][col_name].astype('object')

            elif dtype == 'bool' and not is_bool_dtype(dfs[name][col_name]):
                dfs[name][col_name] = dfs[name][col_name].astype('boolean')

            elif dtype in ('float', 'int') and not is_numeric_dtype(dfs[name][col_name]):
                dfs[name][col_name] = pd.to_numeric(dfs[name][col_name], errors='coerce')

            elif dtype == 'category':
                dfs[name][col_name] = dfs[name][col_name].astype('category')

def clean_data(dfs: dict) -> dict:
    """Load dict with DataFrames as values, clean and
    normalize the data.
    
    Parameters
    ----------
    dfs : dict
        DataFrames stored as dict values
        
    Returns
    ----------
    dict
        cleaned DataFrames stored in dict
    """
    clean_nan(dfs)
    deduplicate(dfs)
    delete_columns(dfs)
    id_index(dfs)
    col_names(dfs)
    clean_url(dfs)
    change_dtypes(dfs)
    
    return dfs
