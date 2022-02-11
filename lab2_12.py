def logic():
    on = ['(', '[', '{']
    off = [')', ']', '}']

    s = str(input())

    result = []
    for i in s:
        if i in on:
            result.append(i)
        else:
            pos = off.index(i)
            if (len(result) > 0) and (result[len(result) - 1] == on[pos]):
                result.pop()
            else:
                return "No"
    if len(result) == 0:
        return "Yes"
    else:
        return "No"
print(logic())