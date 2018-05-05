def sleep_in(weekday, vacation):
  return vacation or not weekday
  
  
  
 def monkey_trouble(a_smile, b_smile):
   return ( a_smile and b_smile) or (not a_smile and not b_smile)
	
	
	
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum
  
  
  
def diff21(n):
  result = abs(n-21)
  if n > 21:
    result = result * 2
  return result
  
  
  
def parrot_trouble(talking, hour):
  return talking and (hour <7 or hour >20)
  
  
  
def makes10(a, b):
  return a == 10 or b == 10 or a+b == 10
  
  

def near_hundred(n):
  return (abs(100 - n) <=10) or (abs(200 - n) <=10)
  
  
  
def pos_neg(a, b, negative):
  if not negative:
    return (a < 0 and b > 0) or (a > 0 and b < 0)
  else:
    return a < 0 and b < 0
	
    
	
def not_string(str):
  if not str[:3] == 'not':
    return 'not ' + str
  return str
  
  
  
def missing_char(str, n):
  return str[:n] + str[n+1:]
  
  
  
def front_back(str):
  if len(str) >=3:
    return str[len(str) -1] + str[1:-1] + str[0]
  elif len(str) == 2:
    return str[1] + str[0]
  else:
    return str



def front3(str):
  return str[:3] * 3