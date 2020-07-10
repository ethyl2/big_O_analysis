def double_print_num(n):
    print(n)
    if n == 0:
        return
    double_print_num(n-1)
    double_print_num(n-1)


double_print_num(3)


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
#
# Time complexity O(2^n)
# You can visualize the calls as a tree, where each function call branches off into 2 more function calls,
# until base case is reached.
