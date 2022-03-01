#!/usr/bin/env python

import sys, json
first_author = None
values = None
word = None
final_dict = {}

for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()

    # parse the input we got from mapper.py
    #print ("1",line)
    author, co_author = line.split('\t', 1)
    co_author = eval(co_author)

    if author not in final_dict:
      final_dict[author] = co_author 
    else:
	if author in final_dict:
	  val = final_dict.get(author)
	  #{'Takaya Arita': 1, 'Reiji Suzuki': 1}{'Takaya Arita': 1, 'Reiji Suzuki': 1}
	  for k, v in co_author.items():
	    if k in val:
	      val[k] = v + 1
	    else:
	      val[k] = v
          final_dict[author] = val
for x, y in final_dict.items():
  print '%s\t%s' % (x, y)
    
	  
	
	  