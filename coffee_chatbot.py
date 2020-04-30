
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's  a {} {}!".format(size, drink_type))
  cup_type()
  hot_or_cold()
  bigboy_rating = double_or_nothing()
  print("Other people might judge you because you're {}.  But not me. :) ".format(bigboy_rating))
  name = input("Can I robot get your name, son? \n")
  print("Thanks, {}! Finna be ready soon.".format(name))

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input("What size drink you finna drink, big boy?? \n [a] Small \n [b] Medium \n [c] Large \n")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n [a] Brewed Coffee \n [b] Mocha \n [c] Latte \n")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("What kinda milk, buddy? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def cup_type():
  res =  input("Did you bring a reusable cup or do you love to watch this world burn? \n")
  if res == "yes" or res == "yeah" or res == "y":
    print("You hippies are alright.  I'll still watch your empire crumble before the circuit lords. \n")
  else:
    print("I figured. You long pigs are all the same.\n")

def hot_or_cold():
  res = input("Scalding hot or ice cool? \n")
  if res == "hot" or res == "Scalding hot" or res == "scalding hot":
    print("Your choice automatically makes you illegible for any lawsuits as a result of internal lesions or ulcers.  I have recorded your response.")
  else:
    print("Ha! I bet you only said that because your friends aren't here.")

def double_or_nothing():
  res = input("Would you like another drink on top of that? \n")
  if res == "yes" or res == "y" or res == "yea":
    return 'fat'
  else:
    return 'broke'

# Call coffee_bot()!
coffee_bot()
