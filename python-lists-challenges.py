#The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
  
print(append_sum([1, 1, 2]))

#The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return(lst1[-1])
  elif len(lst2) > len(lst1):
    return(lst2[-1])
  else:
    return(lst1[-1])


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

## The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(lst1, lst2):
  newlist = lst1 + lst2
  newlist.sort()
  return newlist

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
