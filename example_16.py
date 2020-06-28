def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1
    print(items[last_idx])

    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx:
        print(items[idx])
        idx = idx + 1

    for num in range(20):
        print(num)


do_a_bunch_of_stuff(['pizza', 'toothbrush',
                     'bring me home, country toad', 'spamwich', 'alien Dustin', 'the cake is a lie', 'Gatorade'])

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
# Time complexity: O(n)
# The first print is constant time O(1) b/c it doesn't change as the input changes.
# The while loop that prints up to the middle index is O(n/2), which simplifies to O(n).
# The last print will print the same number of times, no matter the input size, so it is O(1).
# So O(1 + n/2 + 20) simplifies to O(n) because we drop all of the constants.
# Because, as the input sizes gets huge, dividing by 2 or printing something a constant number of times
# has minimal effect on the performance of this algorithm.

# Space O(1)
