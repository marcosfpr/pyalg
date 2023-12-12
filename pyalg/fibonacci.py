def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_bu(n):
    if n < 2:
        return n
    else:
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])
        return fibs[n]


def fib_td(n):
    fibs = [-1 for _ in range(n + 1)]
    return __fib_td(n, fibs)


def __fib_td(n, fibs):
    if fibs[n] != -1:
        return fibs[n]
    else:
        if n < 2:
            fibs[n] = n
        else:
            fibs[n] = __fib_td(n - 1, fibs) + __fib_td(n - 2, fibs)
        return fibs[n]


if __name__ == "__main__":
    n = int(input())

    print("Fibonacci recursive: {}".format(fib(n)))
    print("Fibonacci dynamic programming (bottom-up): {}".format(fib_bu(n)))
    print("Fibonacci dynamic programming (top-down): {}".format(fib_td(n)))
