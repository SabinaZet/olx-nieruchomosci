"""Transform raw data into separate category DataFrames.

Imports
----------
import pandas
import pipeline.config

Returns
----------
dict
    category DataFrames as values
    
Functions
----------
-split_response(page: dict) -> dict
-next_link(request: dict) -> str
-cumulate_data(pages: list) -> list
-data_separate(data: list) -> dict
-normalize_data(separate_data: dict) -> dict
-key_info(dfs: dict)
-clean_nan(dfs: dict) -> dict
-check_data(dfs: dict)
"""

import pandas as pd
import pipeline.config as co

def split_response(page: dict) -> dict:
    """Split first request response into data,metadata,links

    Checks for specified path, so won't work if it changes.

    Parameters
    ----------
    page : dict
        multilevel dict with returned data
        
    Returns
    ----------
    dict
        data, metadata, links wrapped up in a dictionary
    """
    try:
        #lista słowników z produktami
        data = page.get('data').get('clientCompatibleListings').get('data')

        #słownik z metadanymi
        metadata = page.get('data').get('clientCompatibleListings').get('metadata')

        #słownik z linkami do następnej/poprzedniej strony
        links = page.get('data').get('clientCompatibleListings').get('links')
        
        return {
            'data':data,
            'metadata':metadata,
            'links':links
            }
    except:
        print(type(page))

def next_link(request: dict) -> str:
    """Get the URL for next API request.

    If path to link changes, it will break.

    Parameters
    ----------
    request : dict
        data,metadata,links in dict
        
    Returns
    ----------
    str
        URL for next API request
    """
    link = request.get('links').get('next').get('href')
    return link

def cumulate_data(pages: list) -> list:
    """Collect all 'data' values from list of all scraped pages.

    Will break if pages is empty.

    Parameters
    -----------
    pages : list
        all scraped pages
        
    Returns
    ----------
    list
        only 'data' values from pages
    """
    data = []
    for page in pages:
        data.extend(page['data'])
        
    return data

def data_separate(data: list) -> dict:
    """Separate all scraped 'data' values into categories.

    Created for OLX data structure, so will break if it changes.
    Can also break if data list is empty.

    Parameters
    ----------
    data : list
        'data' values from all pages
        
    Returns
    ----------
    dict
        category_name as keys and lists with data as values
    """
    FIELD_MAP = {
    "data_location": [
        "id", "location", "map", "isGpsrAvailable"
    ],
    "data_timing": [
        "id", "last_refresh_time", "created_time",
        "omnibus_pushup_time", "valid_to_time"
    ],
    "data_category": [
        "id", "category", "offer_type"
    ],
    "data_business": [
        "id", "contact", "business", "shop", "user", "protect_phone", "partner"
    ],
    "data_offer": [
        "id", "_nodeId", "location", "title", "status", "url", "description", "external_url"
    ],
    "data_promoted": [
        "id", "promotion"
    ],
    "offer_photos": [
        "id", "photos"
        ],
    "offer_parameters": [
        "id", "params", "key_params"
        ]
    }
    
    separate_data = {name: [] for name in FIELD_MAP}

    for d in data:
        for group_name, fields in FIELD_MAP.items():
            record = {field: d.get(field) for field in fields}
            separate_data[group_name].append(record)

    return separate_data

def normalize_data(separate_data: dict) -> dict:
    """Flatten multilevel dicts into dict with flattened
    cathegorical DataFrames.

    Parameters
    ----------
    separate_data : dict
        data separated into categories in multilevel dicts
        
    Returns
    ----------
    dict
        categories as keys and flattened DataFrames as values
    """
    dfs = {name: pd.json_normalize(records) for name, records in separate_data.items()}
    return dfs

def normalized_data(pages: list) -> dict:
    """Takes list with all scraped data from pages and
    returns dict with DataFrames split into categories.

    Parameters
    ----------
    pages : list
        all scraped pages with data,metadata,links
        
    Returns
    -----------
    dict
        category_name as keys and DataFrames as values
    """
#list with only data values from all pages
    data = cumulate_data(pages)    
#dict with data split into categories by FIELD_MAP
    separate_data = data_separate(data)
#dict with categories as keys and flattened DataFrames as values
    separate_dfs = normalize_data(separate_data)
    
    return separate_dfs
