'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''
def count_evens(nums):
  counts = 0
  for i in range(len(nums)):
    if nums[i] %2 == 0:
      counts += 1
    else:
      continue
  return(counts)

'''Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8'''

def big_diff(nums):
  diff = max(nums) - min(nums)
  return(diff)

'''Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3''''

def centered_average(nums):
  min1 = nums[0]
  max1 = nums[0]
  sum1 = 0
  for x in nums:
    max1 = max(max1, x)
    min1 = min(min1, x)
    sum1 += x
  return (sum - max1 - min1) / (len(nums) - 2)

'''Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6'''

def sum13(nums):
  nums += [0]
  tot=sum(x for y, x in enumerate(nums) if x != 13 and nums[y-1] != 13)
  return tot

