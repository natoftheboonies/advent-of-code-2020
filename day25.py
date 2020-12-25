#!/usr/bin/env python3

from itertools import count

divisor = 20201227

subject = 7

result = 1

#search = (5764801,17807724)
search = (5107328,11349501)

found = []
for x in count(1):
    result = (result*subject)%divisor
    if result in search:
        found.append(x)
    if len(found)==2:
        break
a, b = found
print(a,b)

#print(result)
subject = result
for x in range(a-1):
    result = (result*subject)%divisor
    #print(x, result)

print("#1",result)