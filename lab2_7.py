a = int(input())
demons = {
}
list_demons = []
for i in range(a):
    l = input().split(" ")
    s = str(l[1])
    if s in demons:
        demons[s] = demons[s] + 1
    else:
        demons[s] = 1
        list_demons.append(s)

b = int(input())
slayers = {
}
list_slayers = []
for i in range(b):
    l = input().split(" ")
    s = str(l[1])
    a = int(l[2])
    if s in demons:
        demons[s] = demons[s] - a
sum = 0
for i in list_demons:
    if demons[i] > 0:
        sum += 1
print("Demons left: " + str(sum))