# This function should print the first three multiples of num. Then, it should return the third multiple.
 
def first_three_multiples(num):
  print(num, (num * 2), (num * 3))
  return (num * 3)

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  tip = total * (percentage/100)
  return tip
  
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.


def introduction(first_name, last_name):
  introduction = (last_name + ", " + first_name + " " + last_name)
  return introduction

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# The function should compute the age in dog years and return the following string: "{name}, you are {age} years old in dog years"

def dog_years(name, age):
  dog_years = (name + ", you are "  + str(age * 7) + 
" years old in dog years")
  return dog_years
  
  print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


#Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
#First, print the sum of a and b.
#Second, print d subtracted from c.
#Third, print the first number printed, multiplied by the second number printed.
#Finally, return the third number printed mod a.


def lots_of_math(a,b,c,d):
  first = a + b
  second = c - d
  third = first * second
  print(first)
  print(second)
  print(first * second)
  return third % a
  
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
