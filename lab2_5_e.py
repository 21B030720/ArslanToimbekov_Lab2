s = str(input())
l = s.split(" ")
if len(l) == 1:
    s1 = str(input())
    l.append(s1)
n = int(l[0])
x = int(l[1])
arr = []
for i in range(n):
    a = int(x + 2 * i)
    arr.append(a)
result = arr[0]
for i in range(1, n):
    result ^= arr[i]
print(result)
