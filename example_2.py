# Binary Search
# JS version:
'''
var doSearch = function(array, targetValue) {    
  var minIndex = 0;    
  var maxIndex = array.length - 1;    
  var currentIndex;    
  var currentElement;
  while (minIndex <= maxIndex) {        
      currentIndex = (minIndex + maxIndex) / 2 | 0;        
      currentElement = array[currentIndex];        
      if (currentElement < targetValue) {            
          minIndex = currentIndex + 1;        
      } else if (currentElement > targetValue) {            
          maxIndex = currentIndex - 1;        
      } else {            
          return currentIndex;        
      }    
  }    
return -1;  //If the index of the element is not found.
};
'''
# Python version


def do_search(arr, target):
    min_index = 0
    max_index = len(arr) - 1
    while min_index <= max_index:
        curr_index = (min_index + max_index)//2
        curr_value = arr[curr_index]
        if curr_value == target:
            return curr_index
        elif curr_value < target:
            min_index = curr_index + 1
        elif curr_value > target:
            max_index = curr_index - 1
    return -1


numbers = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
print(do_search(numbers, 23))  # 6

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
# O(log n) time b/c is a binary search
# A logarithmic algorithm halves the input every time it’s run.
# O(1) space
