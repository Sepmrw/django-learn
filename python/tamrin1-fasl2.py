from random import randint

s = input()
v = int(s)
d = randint(0, v)


def odd_or_even(x):
    if int(x) % 2 == 0:
        print("even")
    else:
        print("odd")


print(int(d))
odd_or_even(d)
