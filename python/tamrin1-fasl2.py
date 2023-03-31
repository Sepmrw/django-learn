from random import randint

d = randint(0, 100)


def odd_or_even(x):
    if int(x) % 2 == 0:
        print("even")
    else:
        print("odd")


print(int(d))
odd_or_even(d)
