#!/usr/bin/python3
d={"+":'x+y','-':'x-y','*':'x*y','/':'x/y if y!=0 else "divided by zero"'}
x=int(input())
n=input().strip()
y=int(input())
print(eval(d.get(n)))