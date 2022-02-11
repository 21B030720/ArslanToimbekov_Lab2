ch = ['ONE', 'TWO', 'THR', 'FOU', 'FIV', 'SIX', 'SEV', 'EIG', 'NIN', 'ZER'] # dhfggafjhagfkjahsfkyafku
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
s1 = ""
sum = 0
s = str(input())
l = s.split("+")
for j in range(len(l)):
    for i in range(len(l[j]) - 2):
        if l[j][i:i + 3] in ch:
            pos = ch.index(l[j][i:i + 3])
            s1 += str(num[pos])
    #print(s1)
    sum += int(s1)
    s1 = ""
sum = str(sum)
#print(sum)
for i in sum:
    pos = num.index(int(i))
    print(ch[pos], end = "")
