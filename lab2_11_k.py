s = str(input())
l = set(s.split(" "))
l = sorted(l)

for i in range(len(l)):
    if not l[i].isalpha():
        l[i] = l[i][:-1]
print(len(l))


for i in l:
    print(i)
