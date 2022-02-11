a = int(input())
if a % 2 == 1:
    num = 1
    for i in range(a):
        for j in range(a - num):
            print('.', end = '')
        for j in range(num):
            print('#', end = '')
        print()
        num += 1
else:
    num = 1
    for i in range(a):
        for j in range(num):
            print('#', end='')
        for j in range(a - num):
            print('.', end='')
        print()
        num += 1
