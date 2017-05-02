a_list = [i for i in range(100, 1000) if (i // 100)**3 + (i // 10 % 10)**3 + (i % 10)**3 == i]
print(a_list)
b_list = [i for i in range(100, 1000) if sum(int(s)**3 for s in str(i)) == i]
print(b_list)
c_list = [i for i in range(100, 201) if 0 not in [i % k for k in range(2, i)]]
print(c_list)