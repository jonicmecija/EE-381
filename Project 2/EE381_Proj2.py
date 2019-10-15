'''
EE 381 Fall 2019
Project 2

Jonic Mecija
014467048
Start Date: September 11, 2019
End Date: September 26, 2019

Description: Write te code for the pseudorandom number generator (RNG).
 Use the RNG to solve probability problems. This is problem 1.
'''
import math
import time

t = time.process_time()

#print(int(10000*t))
#Constants for RNG
N = 100000 # the norm
A = 4857 # the adder
M = 8601 # the multiplier
S = int(10000*t)
Ball = [0,0,0] # initially balls not cans
Sum = 0

E = int(input('How man experiments?'))

for j in range(E):
    for i in range(3):
        S = (M* S + A) % N
        r = S/N
        canNumber = math.floor(5*r+1)
        Ball[i] = canNumber
    if (Ball[0] != Ball[1]) and (Ball[1] != Ball[2]) and (Ball[0] != Ball[2]):
        Sum +=1 

prob = Sum / E
print('Probability: ', prob)


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


# simulate die
for i in range(100):
    S = (M * S + A) % N
    r = S/N

    die = math.floor(6*r+1)
    print(die)

'''
