'''
  Copyright (c) 2017 Kartikeya Sharma
  Copyright (c) 2017 Radhika Sood
  Copyright (c) 2017 Harsh Tiku
'''
import re

def remove_extra_spaces(input_string):
    """input: string as input
       removes extra white space like tabs and more than 1 consecutive  space.
       output: string with no extra white spaces
    """
    return ' '.join(input_string.split())
    

def remove_unwanted_suffix(input_string):
    """input: string
       output: string
    """
    return ''.join(input_string[:-4])
   

def remove_non_ascii_letters(input_string):
    """input:string
       output:string
    """
    return ''.join(i for i in input_string if ord(i)<128)

def get_formated_meaning(input_string):
    """input: string
       output: string
    """
    r=remove_extra_spaces(input_string)
    s=remove_non_ascii_letters(r)
    newlinesinserted = re.sub(r"([0-9]+)", r"\n \1", s)
    return newlinesinserted

def get_formated_synonyms(input_string):
    """input: string
       output: list of synonyms
    """
    l=input_string.split('\n')
    synonyms=[]
    for i in l:
     s=remove_unwanted_suffix(i)
     if not len(s)<=0 :
         synonyms.append(s)
    return synonyms

def get_last_word(string):
 string=string.rstrip()
 try:
  x=string.rindex(",")
  newstr=string[x+1:]
 except:
   try:
    x=string.rindex(" ")
    newstr=string[x+1:]
   except: pass
   try: 
    x=string.rindex("(")
    newstr=string[x+1:-1]
   except: pass
 return newstr


def replace_last_word(replace,string):
 string=string.rstrip()
 try:
  x=string.rindex(" ")
 except:
  x=string.rindex(",")
 string=string[:x+1]+replace
 return string

'''
    
 try:
  x=string.rindex(",")
  newstr=string[x+1:]
 except:
   try:
    x=string.rindex(" ")
    newstr=string[x+1:]
   except: 
    x=string.rindex("(")
    newstr=string[x+1:-1]
 return newstr
'''

def str_cmp(a,b):
    if(a.tolower()==b.tolower()):
        return True
    return False
