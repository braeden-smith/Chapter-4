#Braeden Smith Chapter 4 Excercise 6

'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

def computepay():
  hours = float(input('Enter how many hours have you worked:' ))
  rate = float(input('Enter how much your hourly wage is:' ))
  if hours > 40:
    extra = float(hours) - 40
  else:
      extra = 0
  extra_pay = 0.5 * float(rate) * extra

  pay = float(hours) * float(rate) + extra_pay
  
  print ('Your check is: ',pay, 'dollars')
  
computepay()
