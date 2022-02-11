a = int(input())
sum = 0
result = []

for i in range(a):
    s = str(input())
    tU, tL, tN = False, False, False
    for j in s:
        if j.isupper():
            tU = True
        elif j.islower():
            tL = True
        elif j.isdigit():
            tN = True
    if tU and tL and tN:
        if s not in result:
            result.append(s)
            sum += 1
result.sort()
print(sum)
for i in result:
    print(i)
