def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count



def big_diff(nums):
  maxValue = max(nums)
  minValue = min(nums)
  return maxValue - minValue



def centered_average(nums):
  maxValue = max(nums)
  minValue = min(nums)
  total = sum(nums) - (maxValue+minValue)
  return total / (len(nums)-2)
  
  
  
def sum13(nums):
  for i in range(len(nums)-1):
    if nums[i] == 13:
      nums[i] = 0
      nums[i+1] = 0
  if len(nums) >= 1 and nums[len(nums)-1] == 13:
    nums[len(nums)-1] = 0
  return sum(nums)
  
  
  
def sum67(nums):
  for i in range(len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i, len(nums)):
        if nums[j] == 7:
          nums[j] = 0
          break
        else:
          nums[j] = 0
  return sum(nums)
  
  
  
def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False