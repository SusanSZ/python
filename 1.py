m=3
n=8
s=input().split()
a=[int(i) for i in s]
a1=[0]
d=0
for i in range(1,n):
    d+=a[i-1]
    a1.append(d)
sch=[0]*m
search(0)
def search(pos):
    if n-c==0:
        return
    for i in range(n):
        if flag[i] == 0:
            
            flag[i] = 1
            search(pos+1)
            flag[i] = 0
def dis():
    global a1,sch
    mindis=0
    for i in range(n):
        if i<sch[0]:
            d=a1[sch[0]]-a1[i]
        if i>sch[m-1]:
            d=a1[i]-a1[sch[0]]
        for j in range(m):
            if i<=sch[j]:
                d=min(a1[i]-a1[j-1],a1[j]-a1[i])
                break
        mindis+=d
    return mindis