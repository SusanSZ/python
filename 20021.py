#!/usr/bin/python3
a=int(input())
strlen=0
for i in range(1,a+1):
    s=input()
    if len(s)>strlen:
        strlen=len(s)
print('length=%d'%(strlen))