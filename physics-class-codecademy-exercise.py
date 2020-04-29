## just a quick exercise on my way to building a chatbot ## 

train_mass = 22680
train_acceleration = 10
train_distance = 100

c = 3*10**8
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = float((f_temp - 32) * 5/9)
  return c_temp

def c_to_f(c_temp):
  f_temp = float((c_temp * 9/5) + 32)
  return f_temp

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

def get_energy(mass, c):
  energy = mass * (c ** 2)
  return energy

def get_work(mass, acceleration, distance):
  force = mass * acceleration
  work = force * distance
  return work

########--test runs--##########################

f100_in_celsius = float(f_to_c(100))
print(f100_in_celsius)

c0_in_fahrenheit = float(c_to_f(0))
print(c0_in_fahrenheit)
train_force= get_force(train_mass, train_acceleration)

bomb_energy = (get_energy(bomb_mass, c))

train_work = get_work(train_mass, train_acceleration, train_distance)

###########--questions answered--#################################

print("The GE train supplies " + str(train_force) + " Newtons of force")

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
