'''
  Copyright (c) 2017 Kartikeya Sharma
'''

from thesScript import *
from localData import *
from stringProcessing import *
def data_manager_get_synonyms(word):
    if not len(word)<=2: 
        if not local_data_is_excluded_word(word):
            if(local_data_is_word_present(word)):
                return local_data_get_synonyms(word)
            else:
                synonyms=thes_script_get_synonyms(word)
                if(len(synonyms)<=0):
                    local_data_store_excluded_word(word)
                else:
                    local_data_store_word(word,synonyms)
                    if not local_data_synonyms_mapping_exists(word):
                        local_data_store_synonyms_mapping(word,synonyms)
                        return synonyms

#while(True):
#    inp=input("enethr word: ")
#    print(data_manager_get_synonyms(inp))
