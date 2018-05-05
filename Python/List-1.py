def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6
  
  
  
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[len(nums)-1]:
      return True
  return False
  
  
  
def make_pi():
  return [3,1,4]
  
  
  
def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]
  
  
  
def sum3(nums):
  return sum(nums)
  
  
  
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]



def reverse3(nums):
  return [nums[2], nums[1], nums[0]]
  
  
  
def max_end3(nums):
  maxValue = max(nums[0], nums[len(nums)-1])
  return [maxValue, maxValue, maxValue]
  
  

def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
	
	
	
def middle_way(a, b):
  return [a[1], b[1]]
  
  
  
def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]
  
  
  
def has23(nums):
  if nums[0] == 2 or nums[1] == 2:
    return True
  elif nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False