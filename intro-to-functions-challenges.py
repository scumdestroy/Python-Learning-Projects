## create function that does x to the tenth power

def tenth_power(num):
  num = num ** 10
  return num


## create a square root function with the exponent operator **
  
  def square_root(num):
  return num ** 0.5

## create a wins/total games played function

def win_percentage(wins, losses):
  win_percentage = wins / (wins + losses)
  win_percentage = int(win_percentage * 100)
  return win_percentage
  

## create a function for calculating the average of two numbers

  def average(num1, num2):
  average = ((num1 + num2)/2)
  return average


## create a function for finding the remainder of double num1 over half of num2

def remainder(num1, num2):
  remainder = (num1 + num1) % (num2 * 0.5)
  return remainder
