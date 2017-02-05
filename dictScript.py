'''
  Copyright (c) 2017 Kartikeya Sharma
  Copyright (c) 2017 Harsh Tiku
'''

import requests,bs4

from stringProcessing import *

def dict_script_fetch_word(word):
    try:
        response=requests.get('http://www.dictionary.com/browse/'+word)
        response.raise_for_status()
        fetched_data=bs4.BeautifulSoup(response.text)
        elements=fetched_data.select('section[class="def-pbk ce-spot"]')
        return elements[0].getText()
    except (requests.HTTPError , requests.ConnectionError):
        return ''

def dict_script_get_fetched_string(word):
    return dict_script_fetch_word(word)

def dict_script_get_meaning(word):
    meaning=dict_script_get_fetched_string(word)
    if len(meaning)>0:
        return get_formated_meaning(meaning)
    else:
        return ''

