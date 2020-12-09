'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
'''
def cigar_party(cigars, is_weekend):
  if is_weekend == False:
    if cigars in range(40,61):
      return True
    else: return False
  else:
    if cigars >=40:
      return True
    else: return False
    
 '''
 
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).


date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
'''
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you in range(3, 8) and date in range(3,8):
    return 1
  elif (you in range(8, 11) and date in range(8,11)) or (you in range(8,11) or date in range(8,11)):
    return 2
    
'''

The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
'''

def squirrel_play(temp, is_summer):
  if is_summer == True: 
    upperlimit = 100
  else:
    upperlimit = 90
  
  if temp >= 60 and temp <= upperlimit:
    return True
  else:
    return False
    
'''
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.


caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
'''
def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed in range(0, 66):
      return 0
    elif speed in range(65, 86):
      return 1
    else:
      return 2
  else:
    if speed in range(0, 61):
      return 0
    elif speed in range(61, 81):
      return 1
    else:
      return 2
 '''
 Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
'''
def sorta_sum(a, b):
  s = a+b
  if s in range(10,20):
    return 20
  else:
    return int(s)
 
 '''
 Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

'''


    
