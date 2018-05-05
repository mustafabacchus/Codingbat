def double_char(str):
  result = ""
  for i in str:
    result = result + (i * 2)
  return result



def count_hi(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      count += 1
  return count



def cat_dog(str):
  catCnt = 0
  dogCnt = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      catCnt += 1
    if str[i:i+3] == 'dog':
      dogCnt +=1
  if catCnt == dogCnt:
    return True
  return False



def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i: i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count



def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)
  
  
  
def xyz_there(str):
  for i in range(len(str)-3):
    if str[i:i+3] == 'xyz' and not str[i-1] == '.':
      return True
  if str[len(str)-3:] == 'xyz' and not str[len(str)-4] == '.':
    return True
  return False