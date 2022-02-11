l1 = input().split()
l = []

for i in l1:
    l.append(i)


def ars(l):
    max = 0
    pos = 0
    while len(l) > pos:
        if pos > max:
            return False
        if pos + int(l[pos]) > max:
            max = pos + int(l[pos])
        if max >= len(l) - 1:
            return True
        pos += 1


if ars(l):
    print("1")
else:
    print("0")