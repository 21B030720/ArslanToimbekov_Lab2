ot = []
def logic(s):
    p = s[2] + s[1] + s[0]
    ot.append(float(p))
    return int(p)

s = input().split(" ")
result = []
while(s[0] != "0"):
    result.append(s)
    s = input().split(" ")

result.sort(key = logic)
for i in result:
    print("{} {} {}".format(i[0], i[1], i[2]))
#print(ot)