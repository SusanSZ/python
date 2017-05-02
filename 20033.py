a = input().strip()
s = list(filter(lambda x: x.isalpha(), a))
L1 = list()
for i in s:
    if not i in L1:
        L1.append(i)
L1=''.join(L1)
if len(L1)>=10:
    print(L1[:10])
else:
    print('not found')