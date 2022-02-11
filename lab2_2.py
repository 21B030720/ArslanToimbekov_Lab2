a = int(input())
s = str(input())
l = s.split(" ")
max = int(l[0]) * int(l[1])
for i in range(len(l)):
    for j in range(len(l)):
        if i != j and int(l[i]) * int(l[j]) > max:
            max = int(l[i]) * int(l[j])
print(max)