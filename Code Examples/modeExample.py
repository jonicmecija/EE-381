'''
Jonic Mecija
August 28, 2019
EE 381

Description: This is a method on how to get the mode.
'''
# how to get the mode 
nums = [3,4,5,7,7,7,1,1,1]

from collections import Counter

c = Counter(nums) #creates tuples of elements in the list (not mutable)
print(c)
freq = c.most_common() #most common method
print(freq)
max_occur = freq[0][1] #second element of tples will be max assigned

if max_occur != 1:
    modes = [] #empty list 

    for m in freq:
        if m[1] == max_occur: # second position in tuple equal to max_occur
            modes.append(m[0])
    
    print("The mode(s) are: ", modes)

else:
    print("There is no mode.")