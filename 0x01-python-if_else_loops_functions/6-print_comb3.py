#!/usr/bin/pyhton3
for x in range(0,10):
    for y in range(x+1,10):
        if x == 8 and y == 9:
            print("89")
        else:
            print(f"{x}{y}, ",end = "")

