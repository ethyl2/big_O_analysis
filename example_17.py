def do_different_things(items):
    print('1st part:')

    for item in items:
        print(item)

    print('\n2nd part: ')

    for item_one in items:
        for item_two in items:
            print(item_one, item_two)


do_different_things(['lampshade', 'pipecleaner', 'Drano', 'sorting hat',
                     'fun bus', 'struggle bus', 'jello', 'funeral potatoes', 'axelotl'])

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
#
#
#
# Time: O(n^2) b/c O(n + n^2) is simplified to O(n) since we keep only the most significant term.
# Space: O(1)
