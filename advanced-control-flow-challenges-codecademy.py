# Create a function named in_range() that has three parameters named num, lower, and upper.

# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False


# Create a function named same_name() that has two parameters named your_name and my_name.

# If our names are identical, return True. Otherwise, return False.


def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False


# Create a function named always_false() that has one parameter named num.

# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

def always_false(num):
  if num > num or num < num:
    return True
  else:
    return False


# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"


def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"


# Create a function called max_num() that has three parameters named num1, num2, and num3.

# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3):
  if num1 == num2 and num1 > num3:
    return "It's a tie!"
  elif num1 == num3 and num1 > num2:
    return "It's a tie!"
  elif num2 == num3 and num2 > num1:
    return "It's a tie!"
  elif num1 > num2 and num1 > num3:
    return num1
  elif num2 > num3 and num2 > num1:
    return num2
  else:
    return num3
