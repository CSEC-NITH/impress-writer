'''
  Copyright (c) 2017 Kartikeya Sharma
'''
import requests,bs4
from stringProcessing import *

def thes_script_fetch_word(word):
    try:
        response=requests.get('http://www.thesaurus.com/browse/'+word)
        response.raise_for_status()
        fetched_data=bs4.BeautifulSoup(response.text)
        elements=fetched_data.select("div[class='relevancy-list']")
        return elements[0].getText()
    except (requests.HTTPError , requests.ConnectionError):
        return ''
        
def thes_script_get_fetched_string(word):
    return  thes_script_fetch_word(word)

def thes_script_get_synonyms_list(response):
    return get_formated_synonyms(thes_script_get_fetched_string(response))

def thes_script_get_synonyms(word):
    return thes_script_get_synonyms_list(word)

'''while(True):
    inp=input("enter word:")
    print (thes_script_fetch_word(inp))
'''
