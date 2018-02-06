#!/bin/python3
'''

def counterGame(n):
    # Complete this function
    winner=["Richard","Louise"]
    result = n & (n-1)
    if result == 0:


        return n

    else :


        return winner[0]

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = counterGame(n)
        print(result)

'''
import sys




#https://www.hackerrank.com/challenges/counter-game/problem

import sys

players = "Richard", "Louise"

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
  # Based on awesome solution from AbhishekVermaIIT
    print(players[bin(N-1).count("1")%2])