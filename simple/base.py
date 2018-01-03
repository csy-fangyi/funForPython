# -*- coding: utf-8 -*-

a = list(range(1, 100))
print(a)

print(a[1::5])

a = [x * x for x in range(1, 11)]
print(a)
print(isinstance(a, str))

g = (x * x for x in range(10))
for x in g:
    print(x)

print('fib-----')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


fib(10)

print('fib2-----')


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for x in fib2(10):
    print(x)

print('triangel----')


def triangel(n):
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > 10:
            break


g = triangel(10)
print(g)

for x in g:
    print(x)
