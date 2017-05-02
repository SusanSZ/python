name=('knave','knight')
for v in range(0, 3):
    a = v // 2
    b = v % 2
    if a == b & b == (a != b):
        print("A is a {0},B is a {1}".format(name[a],name[b]))