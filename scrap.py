#
from random import randint

with open(r'C:\Users\genestb\Documents\adj.txt') as infile:
    data=[element.rstrip() for element in infile]
    adj=data

with open(r'C:\Users\genestb\Documents\noun.txt') as infile:
    data1=[element.rstrip() for element in infile]
    noun=data1

l = len(adj) - 1
L = len(noun) - 1

y = adj[randint(0,l)]
x = noun[randint(0,L)]
print(y,x)
