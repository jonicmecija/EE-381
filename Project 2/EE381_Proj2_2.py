'''
EE 381 Fall 2019
Project 2

Jonic Mecija
014467048
Start Date: September 16, 2019
End Date: September 26, 2019

Description: Project 2 Problem 2.
'''
import math
import time

def main():
        success = 0
        failure = 0

        for i in range(1000000):
                x = diceroll()

                try:
                        three = x.index(3)
                        a = three + 1
                        success = success + a
                except:
                        b = len(x)
                        failure += b
        p = success / (success + failure)
        print("Probability of sum of three before sum of 7:", p)

def diceroll():
        #Constants for RNG
        N = 100000 # the norm
        A = 4857 # the adder
        M = 8601 # the multiplier

        Z = 0
        Rolls = []

        while Z != 7:
                
                S_1 = time.perf_counter_ns()%999999
                S_1 = (M * S_1 + A) % N
                r = S_1/N
                die_1 = math.floor(6*r+1)

                S_2 = time.perf_counter_ns()%10000
                S_2 = (M * S_2 + A) % N
                r = S_2/N
                die_2 = math.floor(6*r+1)

                Z = die_1 +die_2
                Rolls.append(Z)

        return Rolls

main()