# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:31:42 2016

@author: ericgrimson
"""

'''''
•Solve a smaller problem
•Solve a basic problem
•Solve a smaller problem
'''''

counter = 1
def printMove(fr, to):
    global counter
    print(str(counter) + ': move from ' + str(fr) + ' to ' + str(to))
    counter += 1

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))