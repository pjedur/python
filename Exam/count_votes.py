import os
import csv
def count_votes(s):
    x = 10
    d= {}
    l = []
    with open(s,"r") as f:
        r = csv.reader(f, delimiter=' ', quotechar='"')
        for i in r:
            if x == 0:
                break
            else: 
                l.append(i)
                x -=1
    return l
    '''
            if x == 0:
                break
            else:
                #i = i.split('"')
                print(i)
                x-=1
                '''
    '''x = open(s, encoding="8859-1", "r")
    x = x.readlines()
    for i in x:
        print(i)
    print(23'''
