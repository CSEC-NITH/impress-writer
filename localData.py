#!/usr/bin/python3
'''
  Copyright (c) 2017 Kartikeya Sharma
  Copyright (c) 2017 Radhika Sood
'''
#like is,as,the (a set)
from stringProcessing import *

excluded_words=set()

#like beautiful:[divine,facinating] (dict of string ,list of string)
words_data={}

#like divine:beautiful (dict of string:string)
#     facinating:beautiful
synonyms_mapping={}

def local_data_load_excluded_words():
    file=open('excludedWords.txt','r')
    for lines in file.readlines():
     l=lines.split()
     excluded_words.update(l)
    return excluded_words
    

def local_data_load_words_data():
    file=open('wordsData.txt','r')
    words=[]
    for lines in file.readlines():
     l=lines.rstrip()
     words.append(l)
    i=0
    for w in range(len(words)):
     if(i!=len(words)):
      key=words[i]
      i+=1
      no_of_synonyms=int(words[i])
      i+=1
      value=[]
      for count in range(no_of_synonyms):
         value.append(words[i])
         i+=1
      words_data[key]=value
    file.close()
    return words_data
 
def local_data_load_synonyms_mapping():
    i=0
    for w in words_data:
     for i in words_data[w]:
      synonyms_mapping[i]=w
    return synonyms_mapping


def local_data_init():
    local_data_load_excluded_words()
    local_data_load_words_data()
    local_data_load_synonyms_mapping()

def local_data_is_word_present(word):
    return word in words_data.keys()

def local_data_is_excluded_word(word):
    return word in excluded_words

def local_data_store_word(word,synonyms):
    word.lower()
    words_data[word]=synonyms[:]
    file=open('wordsData.txt','a')
    file.write(word+'\n')
    file.write(str(len(synonyms)).lower()+'\n')
    for syn in synonyms:
        file.write(syn.lower()+'\n')
    file.close()

def local_data_store_excluded_word(word):
    excluded_words.add(word)
    file=open('excludedWords.txt','a')
    file.write(word+'\n')
    file.close()

def local_data_store_synonyms_mapping(word,synonyms):
    pass
'''
    file=open('synonymsMapping.txt','a')
    for syn in synonyms:
        synonyms_mapping[syn]=word
        file.write(syn+'\n')
        file.write(word)
    file.close()
'''
def local_data_synonyms_mapping_exists(word):
    return word in synonyms_mapping.keys()
    

def local_data_get_synonyms(word):
    if word in words_data.keys():
     return words_data[word]

'''
print(local_data_load_excluded_words())
print(local_data_load_words_data())
print(local_data_is_word_present("ASVD"))
print(local_data_load_synonyms_mapping())
print(local_data_synonyms_mapping_exists('10'))
print(local_data_get_synonyms('add'))
print(local_data_get_synonyms('ASVD'))
#print(local_data_get_synonyms("ASDV"))
#print(local_data_is_excluded_word("is"))
#local_data_store_word("asdf jdkcn",['8','9','10','11','12'])
#local_data_store_word("asdf",['3we','svc2','dfsa3','cv4'])
'''
