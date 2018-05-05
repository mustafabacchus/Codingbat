def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  if not is_weekend and cigars >=40 and cigars <=60:
    return True
  return False
  
  
  
def date_fashion(you, date):
  if you <=2 or date <=2:
    return 0
  if you >=8 or date >= 8:
    return 2
  return 1
  
  
  
def squirrel_play(temp, is_summer):
  if not is_summer and temp >=60 and temp <=90:
    return True
  if is_summer and temp >=60 and temp <=100:
    return True
  return False
  
  
  
def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    elif speed >= 81:
      return 2
    else:
      return 1
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed >= 86:
      return 2
    else:
      return 1
	  
	  
	  
def sorta_sum(a, b):
  sum = a + b
  if sum >=10 and sum <=19:
    sum = 20
  return sum
  
  
  
def alarm_clock(day, vacation):
  if not vacation and (day >=1 and day <=5):
    return '7:00'
  if vacation and (day == 0 or day == 6):
    return 'off'
  return '10:00'
  
  
  
def love6(a, b):
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6
  
  
  
def in1to10(n, outside_mode):
  if outside_mode:
    return n <=1 or n >=10
  if not outside_mode:
    return n >=1 and n <=10
	
	
	
def near_ten(num):
  temp = num % 10
  return temp <=2 or temp >=8