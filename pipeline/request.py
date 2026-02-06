"""Sending requests to API and collecting returned JSON
data from all the pages sorted by the latest date of adding.

Imports
----------
import requests
import pipeline.config
import pipeline.transform

Returns
----------
list
    dicts with data, metadata and links of scraped pages

Functions
----------
-request() -> dict
-fetch_next_page(next_url: str) -> dict
-paginate() -> list
"""

import requests
import pipeline.config as co
import pipeline.transform as pt

def request() -> dict:
    """Post first POST request to API.
    Prints if status code is not 200.

    Returns
    ----------
    dict
        data, metadata, links wrapped up in a multi level format
    """
    response = requests.post(co.url, headers=co.headers,
                             json=co.json_data)

    if response.status_code != 200:
        print("Response status code: ", response.status_code)
    
    
    return response.json()

def fetch_next_page(next_url: str) -> dict:
    """Sends GET request to API using provided link.
    Prints status code.

    Can fail if bad dtype or no link provided.

    Parameters
    ----------
    next_url : str
        URL to direct API request
        
    Returns
    ----------
    dict
        data, metadata, links wrapped up in a dictionary
    """
    response = requests.get(next_url, headers=co.headers)
    
    if response.status_code != 200:
        print("Status code: ", response.status_code)
    return response.json()


def paginate() -> list:
    """Send requests to API and collect received data.
    Next extract the 'next_link' value from 'links' to send
    with next API request.

    Prints message when request error occurs.
    Prints message when error with getting the link occurs.

    Ends proceeding when no link found in the
    ['links']['next']['href'] so it can crash here
    (data structure can be different somewhere).

    Returns
    ----------
    list
        dicts with data, metadata, links of each page
    """
    pages = []

#split first multilevel dict into data,metadata,links
    page = pt.split_response(request())
    
    nxt_link = pt.next_link(page)
    pages.append(page)
    
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

