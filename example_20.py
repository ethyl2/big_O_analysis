def triple_print_num(n):
    print(n)
    if n == 0:
        return
    triple_print_num(n-1)
    triple_print_num(n-1)
    triple_print_num(n-1)


triple_print_num(3)

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
# Time O(3^n)
