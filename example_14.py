"""
Input: [10, 20, 10, 5, 15]
Output: [10, 30, 40, 45, 60]
The value of the output_list[i] = input[0] + input[1] + input[2] ... input[i]
"""


def make_prefix_sum_arr1(arr):
    output = []
    output.append(arr[0])
    for i in range(1, len(arr)):
        output.append(output[i-1] + arr[i])
    return output


def make_prefix_sum_arr2(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]
    return arr


print(make_prefix_sum_arr1([10, 20, 10, 5, 15]))
print(make_prefix_sum_arr2([10, 20, 10, 5, 15]))
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
# 1. time O(n) space O(n)
# 2. time O(n) space O(1)
