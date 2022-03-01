#!/usr/bin/env python

import json
import sys

a = sys.stdin
obj=json.load(a)
obj = obj['result']
remove_attributes = ['time', 'completions', 'query', 'status']
hitlist = []

def processData():
    for element in obj.keys():
      if element in remove_attributes:
            del obj[element]

    hits = obj['hits']
    for k,v in hits.items():
	if k == 'hit':
	  obj[k] = v
    del obj['hits']

    for v in obj['hit']:
	for a, b in v['info'].items():
            if a == 'authors':
                hitlist.append(v)
    obj['hit'] = hitlist


def remove_spec_chars(strng):
    for char in strng:
	if not(char in range(65, 91) and char in range(97,123)):
	   strng.replace(char, '')
    return strng

def Convert(a):
    length = len(a)
    author = a[0].encode('utf-8')
    res_dct = {a[i+1].encode('utf-8'): 1 for i in range(0, length -1)}
    return author,res_dct

processData()

for line in obj['hit']:
   a = line['info']['authors']['author']      
   if(isinstance(a, list)):
     arr = []
     for b in a:
       parsed_string = remove_spec_chars(b['text'])
       arr.append(parsed_string)
     auth, result = Convert(arr)
     print '%s\t%s' %(auth, result)