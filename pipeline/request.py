import requests
import re
import pipeline.config as co
import pipeline.transform as pt

#W json_data() można ustawić offset, limit i category_id (int)
def request():
    response = requests.post(co.url, headers=co.headers,
                             json=co.json_data)

    print("Original response type: ", type(response))
    print("Response status code: ", response.status_code)
    
    
    return pt.split_response(response.json())

def fetch_next_page(next_url):
    response = requests.get(next_url, headers=co.headers)
    print("Status code: ", response.status_code)
    return pt.split_response(response.json())


def paginate() -> list:
    pages = []

    page = request()
    pages.append(page)
    offset = 40
    limit = 40
    link = page.get('links').get('self').get('href')
    new_link = re.sub(r"offset=\d+", f"offset={offset}", link)
    total = page.get('metadata').get('total_elements')
    
    while offset <= total:
        
        try:
            page = fetch_next_page(new_link)
            offset += limit
            pages.append(page)
        except:
            print('Błąd na linku: ', new_link)

    return pages

