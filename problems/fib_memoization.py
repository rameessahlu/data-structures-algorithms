def fibHelper(n, d):
    if n not in d and n >= 1:
        d[n] = fibHelper(n-1, d) + fibHelper(n-2, d)
    if n == 1:
        return d[n]+d[1]
    return d[n]

def fib(n):
    return fibHelper(n, {1: 1, 0 : 0})

print('answer', fib(5))