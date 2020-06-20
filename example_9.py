# Merge sort
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i+1
            else:
                alist[k] = right_half[j]
                j = j+1
            k = k+1

        # Checking if any element was left
        while i < len(left_half):
            alist[k] = left_half[i]
            i = i+1
            k = k+1
        while j < len(right_half):
            alist[k] = right_half[j]
            j = j+1
            k = k+1


alist = [11, 22, 55, 44, 77, 66, 44, 33, 88]
merge_sort(alist)
print(alist)

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
# O(n log n) time
