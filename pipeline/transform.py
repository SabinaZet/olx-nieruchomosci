import pandas as pd

def split_response(response: dict):
    #lista słowników z produktami
    data = response.get('data').get('clientCompatibleListings').get('data')

    #słownik z metadanymi
    metadata = response.get('data').get('clientCompatibleListings').get('metadata')

    #słownik z linkami do następnej/poprzedniej strony
    links = response.get('data').get('clientCompatibleListings').get('links')
    
    return {
        'data':data,
        'metadata':metadata,
        'links':links
        }

def cumulate_data(pages: list) -> list:
    data = []
    for page in pages:
        data.extend(page.get('data'))
        
    return data

def data_separate(data: list) -> dict:
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
    dfs = {name: pd.json_normalize(records) for name, records in separate_data.items()}
    return dfs