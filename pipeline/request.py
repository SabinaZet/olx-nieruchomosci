import requests
import pipeline.config as co

#W json_data() można ustawić offset, limit i category_id (int)
def request(**kwargs) -> dict:
    json = co.json_data()
    
    response = requests.post(co.url, headers=co.headers,
                             json=json)

    print("Original response type: ", type(response))
    print("Response status code: ", response.status_code)
    
    return response.json()

#total pobieramy z metadata pierwszego response
def pagination(total: int) -> list:
    offset = 40
    limit = 40
    offers = []
    
    while offset <= total:
        offers.append(request(offset=offset))
        offset += limit
    
    return offers