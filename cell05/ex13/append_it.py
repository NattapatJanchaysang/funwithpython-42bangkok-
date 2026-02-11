#!/usr/bin/env python3
import sys


if len(sys.argv) > 1:
    
    params = sys.argv[1:]
    
    
    found = False
    
 
    for p in params:
       
        if not p.endswith("ism"):
            print(f"{p}ism")
            found = True
            

else:
    
    print("none")