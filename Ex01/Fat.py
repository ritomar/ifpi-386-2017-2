def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f


def fatorial_recursiva(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursiva(n - 1)


def print_fatorial(n):
    for i in range(n, 0, -1):
        if i > 1:
            print("%d x " % i, end="")
        else:
            print("1 = %d" % fatorial(n), end="")



print_fatorial(5)
