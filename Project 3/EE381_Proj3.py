'''
EE 381 Fall 2019
Project 3

Jonic Mecija
014467048
Start Date: September 23, 2019
End Date: September 30, 2019

Description: This project is about Markov Chains in project 3.
This starts with Bernoulli trials.
'''

import random #pythons RNG library

# Simulation of a Bernoulli Random Variable
print("Simulation of a Bernoulli Random Variable")

p = float(input("Enter the probability of success: "))
T = int(input("Enter the number of trials you want to run: "))

print("\n")

#-----------------------------------------------
for j in range(T):
    r = random.uniform(0,1)

    if r < p:
        print("H", end =" ")
    else:
        print("T", end =" ")