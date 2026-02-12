#!/usr/bin/env python3
import sys


if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
   
    occurrence = text.count(keyword)
    
    
    if occurrence > 0:
        print(occurrence)
    else:
        print("none")
else:
    
    print("none")