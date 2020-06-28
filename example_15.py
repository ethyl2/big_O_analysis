# Assume n is an integer


def foo(n):
    print("Added to the call stack with n = " + str(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return foo(n-1) + foo(n-2)


print(foo(10))
# print(foo(73))
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
#
#
#
#
#
# Time O(c^n) aka exponential. As the size of the input increases, the runtime will grow at a much faster rate.
# So it is very inefficient.
# Space O(c^n) I'm assuming, b/c of all of the additional calls added to the call stack, due to recursion.
# Correct me if I'm wrong! 😊
