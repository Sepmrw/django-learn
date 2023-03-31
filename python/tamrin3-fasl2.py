a = input("enter your text: ").replace(" ", '').split()
a = str(a)
d = {"charceters": 0, "numbers": 0}


def counter(a):
    di = li = 0
    for i in a:
        if i.isdigit():
            di += 1
            # print(di)
        elif i.isalpha():
            li += 1
            # print(li)
    return di, li


digit, letter = counter(a)
d["numbers"] = digit
d["charceters"] = letter
print(d)
