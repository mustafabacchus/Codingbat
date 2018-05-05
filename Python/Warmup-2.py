def string_times(str, n):
  return str * n
  
  
  
def front_times(str, n):
  return str[:3] * n
  
  
  
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result



def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
  
  
  
def last2(str):
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count
  
  
  
def array_count9(nums):
  cnt9 = 0
  for i in nums:
    if i == 9:
      cnt9 += 1
  return cnt9
  
  
  
def array_front9(nums):
  if len(nums) >= 4:
    front = nums[:4]
  else:
    front = nums
  if 9 in front:
    return True
  else:
    return False
    
    
    
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
  
  
  
def string_match(a, b):
  count = 0
  for i in range(min(len(a),len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count