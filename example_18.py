def alg(data):
    if data == []:
        return 0

    first_val = data[0]

    return first_val + alg(data[1:])


print(alg([5, 4, 3, 2, 1, 0]))  # 15


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
#
#
#
#
# Time complexity: O(n), I believe.
# Space complexity: O(n^2).
"""
Explanation for space complexity:
"Every time we make a call into alg(), we get new space for local variables. 
So any local variable that was O(1) on its own, now gets n copies and becomes O(1*n) or O(n).

But that's not all. When we slice data on the recursive call, we get a new list. 
So that means every call we're getting another copy of the list, and each copy is O(n) space as well. 
And we're making n recursive calls, so we need n copies of O(n) space, which comes to O(n*n) or O(n^2) space."
"""
"""
"Sure, it's not a complete copy of the list. It's missing the first element. So each call has a shorter and shorter list, like:

[ 1, 2, 3, 4 ]
[ 2, 3, 4 ]
[ 3, 4 ]
[ 4 ]
[ ]
So that means the first call wasn't really O(n), but was more like O(0.8*n), and the second was O(0.6*n), and so on.

But recall that we drop constants with Big-O, so those still just become O(n)."
"""
"""
first_val on its own is O(1). But we recurse n times, so it becomes O(1*n) or just O(n).

Each slice of data on its own is O(n). But we recurse n times, so it becomes O(n*n) or O(n^2).

So the total space complexity for this algorithm is:

O(n) + O(n^2). The O(n^2) dominates, so the final space complexity is just O(n^2).

source: https://github.com/LambdaSchool/cs-module-project-recursive-sorting
"""
