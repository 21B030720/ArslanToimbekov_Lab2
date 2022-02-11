import math


u = input().split(" ")
p_x, p_y = u
p_x = int(p_x)
p_y = int(p_y)
n = int(input())
l = []

def logic(l1):
    global p_x
    global p_y
    x = p_x
    y = p_y
    res1 = math.sqrt( (x-l1[0])**2 + (y-l1[1])**2 )
    return res1


for i in range(n):
    u1 = input().split(" ")
    x, y = u1
    x = int(x)
    y = int(y)
    sub_l = [x, y]
    l.append(sub_l)
l.sort(key = logic)
for i in range(len(l)):
    print(str(l[i][0]) + " " + str(l[i][1]))
