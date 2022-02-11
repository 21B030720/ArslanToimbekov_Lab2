a = int(input())
l1 = []
l2 = []
n = 0
for i in range(a):
    q = input().split()
    if q[0] == '1':
        l1.append(q[1])
    else:
        l2.append(l1[0])
        del l1[0]
for i in l2:
    print(i, end = " ")