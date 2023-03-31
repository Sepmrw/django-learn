d = int(input())


def function(x):
    s = 0
    for i in range(0, x):
        print(i)
        s += i
    return s + x



result = function(d)

print(result)
