a = int(input())
ars = {
}
people = []
for i in range(a):
    l = input().split(" ")
    s = str(l[0])
    a = int(l[1])
    if s in ars:
        ars[s] = ars[s] + int(a)
    else:
        ars[s] = a
        people.append(s)

l = ars.values()
people.sort()
Max = max(l)
for i in people:
    if ars[i] < Max:
        print(i + " has to receive " + str(Max - ars[i]) + " tenge")
    else:
        print(i + " is lucky!")
#result = ars.items()
#print(result)

