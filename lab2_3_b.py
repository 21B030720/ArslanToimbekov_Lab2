l = []
a = int(input())
for i in range(a):
    l.append([])
    for j in range(a):
        l[i].append(0)

for i in range(a):
    l[i][0] = i
    l[0][i] = i
    l[i][i] = i**2
for i in range(a):
    for j in range(a):
        print(l[i][j], end = " ")
    print()


