# CPE 202 Lab 1a
from typing import Optional
from typing import List

# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   count = 0
   if int_list is None:
      raise ValueError
   elif int_list == []:
      return None
   else:
      for _ in int_list:
         count += 1
      return count


# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   else:
      return int_list[::-1]



# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> Optional[List]:
   "-> None"
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   count = -1
   newList: List[float] = []
   if int_list is None:
      raise ValueError
   else:
      for _ in int_list:
         newList.append(int_list[count])
         count -= 1
      print(newList)
      return newList

      # length = len(int_list)
      # if length <= 1:
      #    return int_list
      # return int_list[length - 1:] + reverse_list_mutate(int_list[:length - 1])


# print(reverse_list_mutate([1, 2, 3]))
#       newList = int_list.reverse()
#       return newList

# count = -1
#    newList: List[float] = []