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