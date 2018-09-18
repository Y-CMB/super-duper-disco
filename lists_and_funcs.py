##############################################
##############################################
##################### | ######################
################### | | ######################
################# |   | ######################
##################### | ######################
##################### | ######################
##################### | ######################
############### -------------- ###############
##############################################
##############################################

"""
Create a function named double_index that has two parameters named lst and index.

The function should double the value of the element at index of lst and return the new list with the doubled value.

If index is not a valid index, the function should return the original list.

After writing your function, un-comment the call to the function that we've provided for you to test your results.
"""
#Write your function here
def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 4))

"""
Create a function named remove_middle which has three parameters named lst, start, and end.

The function should return a sub-list of lst with all elements with index between start and end removed (inclusive).

For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

removeMiddle([4, 8 , 15, 16, 23, 42], 1, 3)
"""
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

"""
Create a function named more_than_n that has three parameters named lst, item, and n.

The function should return True if item appears in the list more than n times. The function should return False otherwise.
"""
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

"""
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
"""
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item1) < lst.count(item2):
        return item2
    else:
        return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

"""
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements,
the function should return the average of the middle two elements.
"""
#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

"""
Write a function named append_sum that has one parameter named lst.

The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""
#Write your function here

def append_sum(lst):
    count = 0
    while count < 3:
        lst.append(lst[-2] + lst[-1])
        count += 1
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

"""
Write a function named larger_list that has two parameters named lst1 and lst2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
"""
#Write your function here
def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    elif len(lst1) < len(lst2):
        return lst2[-1]
    else:
        return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""
#Write your function here
def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
Create a function called append_size that has one parameter named lst.

The function should add all of the numbers between 1 and the size of lst (inclusive) to the end of lst. The function should then return this new list.

For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 1, 2, 3] because the size of lst was originally 3.
"""
#Write your function here
def append_size(lst):
    end_lst = list(range(1, len(lst)+1))
    lst += end_lst
    return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

"""
Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.
"""
#Write your function here
def every_three_nums(start):
    if start < 101:
        return list(range(start, 101, 3))
    else:
        return list()

#Uncomment the line below when your function is done
print(every_three_nums(91))
