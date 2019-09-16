'''
EE 381 Fall 2019
Project 2

Jonic Mecija
014467048
Start Date: September 16, 2019
End Date:

Description: Write te code for the pseudorandom number generator (RNG).
 Use the RNG to solve probability problems. This is problem 1.
'''
import math
import time

t = time.process_time()

#Constants for RNG
N = 100000 # the norm
A = 4857 # the adder
M = 8601 # the multiplier

for i in range(10):
        S_1 = int(10000*t)
        S_1 = (M * S_1 + A) % N
        r = S_1/N
        die_1 = math.floor(6*r+1)

        S_2 = int(10000*t)
        S_2 = (M * S_2 + A) % N
        r = S_2/N
        die_2 = math.floor(6*r+1)

        
        print(die_1, die_2)