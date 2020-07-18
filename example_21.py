
def lots_of_nesting(n):
    total = 0
    for i in range(n):
        i += 1
        for j in range(i+1, n):
            j += 1
            for k in range(j+1, n):
                for l in range(k+1, 10+k):
                    l += 1
                    total += 1
    return total


print(lots_of_nesting(25))

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
# Time complexity: O(n^3)
# The first loop is O(n)
# The second loop is basically O(n); same as the third. They would run a little less,
# some fraction times n, but simplify to O(n)
# because we get rid of constants.
# We might see the last loop and think, another O(n), but NO, it always loops 9 times,
# so O(9), a constant, so don't bother with that part.
# So O(n*n*n) = O(n^3)
