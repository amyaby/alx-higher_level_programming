#!/usr/bin/pyhton3
ascii = ord('a')
while ascii <= ord('z'):
    if ascii ==  ord('q') or ascii == ord('e'):
     ascii += 1 # move 'q' or 'e'
     continue # skip the print statement for 'q' & 'e'
    print(chr(ascii),end="")
    ascii += 1 # move to other caracters 
