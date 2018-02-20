#Braeden Smith Chapter 4 Excercise 7

'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
Score   Grade
> 0.9     A
> 0.8     B
> 0.7     C
> 0.6     D
<= 0.6    F
Program Execution:
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
'''

def computegrade():
  num = float(input('Enter in a grade between 0.0 and 1.0:' ))
  try:
    if num >=1.00000001:
      print('Error: only numbers 0.0 to 1.0')
    elif num >= .9:
      print('This grade is an A')
    elif num >= .8:
      print('This grade is an B')
    elif num >= .7:
      print('This grade is an C')
    elif num >= .6:
      print('This grade is an D')
    elif num <= .59:
      print('This grade is an F')
    elif num >= 0:
      print('Error')
  except:
    print ('error_msg_invalid')
    num = input('Enter a score between 0.0 and 1.0: ')
 
computegrade()
