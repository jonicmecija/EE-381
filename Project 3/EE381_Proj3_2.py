'''
EE 381 Fall 2019
Project 3

Jonic Mecija
014467048
Start Date: September 23, 2019
End Date: September 30, 2019

Description: This project is about Markov Chains in project 3.
This starts with Bernoulli trials. We will simulate markov chain.
'''

import random

L = [] # store particle location history
S = random.randint(0,1) # initial location 
L.append(S)

p = float(input('Enter the probability of going from node 0 to node 1.'))
q = float(input('Enter the probability of going from node 1 to node 2.'))


for i in range(24):
    r = random.uniform(0,1)
    # bernoulli r.v. and location

    if S == 0 and r < p:
        S = 1
    elif S == 1 and r < q:
        S = 0

    # below formatting of output 
    L.append(S)

for i in range(25):
    print(L[i], end=' ')
    