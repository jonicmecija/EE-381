'''
EE 381 Fall 2019
Project 2

Jonic Mecija
014467048
Start Date: September 11, 2019
End Date:

Description: Write te code for the pseudorandom number generator (RNG).
 Use the RNG to solve probability problems.
'''
import math

#Constants for RNG
N = 10000 # the norm
A = 4857 # the adder
M = 8601 # the multiplier

S = int(input("Enter a value to start RNG: "))

N = 25


'''

print(S)
for i in range(100):
    S = (M * S + A) % N
    r = S/N
    print(format(r,'.4f'))
'''


'''
# simulate a coin
# possible question on exam

N = 25

for i in range(100):
    S = (M * S + A) % N
    r = S/N

    coin = math.floor(2*r)

    if coin == 0:
        print("T")
    else:
        print("H")
'''

# simulate die
for i in range(100):
    S = (M * S + A) % N
    r = S/N

    die = math.floor(6*r+1)
    print(die)