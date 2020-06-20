# Recursive calculation of Fibonacci numbers
def fibonacci(num):
    if (num <= 1):
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)


print(fibonacci(10))

"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it:

the 2 is found by adding the two numbers before it (1+1),
the 3 is found by adding the two numbers before it (1+2),
the 5 is (2+3),
and so on!
"""
#
#
#
#
#
#
#
#
#
#
# time O(2^n) aka Exponential
# https://medium.com/@cindychen13.work/a-beginners-guide-to-big-o-notation-793d654973d
