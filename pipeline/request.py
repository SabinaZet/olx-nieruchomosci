import requests
import pipeline.config as co
import pipeline.transform as pt

#W json_data() można ustawić offset, limit i category_id (int)
def request():
    response = requests.post(co.url, headers=co.headers,
                             json=co.json_data)

    print("Original response type: ", type(response))
    print("Response status code: ", response.status_code)
    
    
    return response.json()

def fetch_next_page(next_url):
    response = requests.get(next_url, headers=co.headers)
    print("Status code: ", response.status_code)
    return response.json()


def paginate() -> list:
    pages = []

    page = pt.split_response(request())
    nxt_link = pt.next_link(page)
    
    while nxt_link:
        
        try:
            page = fetch_next_page(nxt_link)
            pages.append(page)
            try:
                nxt_link = pt.next_link(page)
            
                if not nxt_link:
                    break
            except:
                print('Błąd na tworzeniu nxt_link')
                break
            
        except:
            print('Błąd na linku: ', nxt_link)
            break

    return pages

