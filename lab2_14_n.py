l = []
result = []
a = int(input())
while(a > 0):
    a = int(a)
    l.append(a)
    a = int(input())
size = int(len(l))
for i in range(size//2 + size%2):
    pos1 = i
    pos2 = len(l)-1-i
    if not pos1 == pos2:
        result.append(l[pos1] + l[pos2])
    else:
        result.append(l[pos1])
for i in result:
    print(i, end = " ")
