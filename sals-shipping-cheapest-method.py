def ground_shipping_cost(weight):
  if weight <= 2:
    ground_cost = (weight * 1.5) + 20
  elif weight <= 6:
    ground_cost = (weight * 3) + 20
  elif weight <= 10:
    ground_cost = (weight * 4) + 20
  else:
    ground_cost = (weight * 4.75) + 20
  return ground_cost

def drone_shipping(weight):
   if weight <= 2:
    ground_cost = (weight * 4.5)
  elif weight <= 6:
    ground_cost = (weight * 9)
  elif weight <= 10:
    ground_cost = (weight * 12)
  else:
    ground_cost = (weight * 14.25)
  return drone_cost

premium_cost = 125 

def cheapest_method(weight):
  gsc = ground_shipping_cost(weight)
  dsc = drone_shipping(weight)
  if gsc < dsc and gsc < 125:
    return "Ground Shipping be your best bet, big boy."
  elif dsc < gsc and gsc < 125:
    return "Drone Shipping be ya boy there"
  elif gsc > 125 and dsc > 125:
    return "Premium ya go - somehow??"
  else:
    return "IDK WTF HAPPENED LOL"

print(cheapest_method(4.8))

print(cheapest_method(41.5))
