arr = [2, 16, 7, 9, 8, 23, 12]


def find_max_of_unsorted_arr(a):
    max_item = a[0]
    for item in a:
        if item > max_item:
            max_item = item
    return max_item


print(find_max_of_unsorted_arr(arr))
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
# O(n) time, O(1) space
