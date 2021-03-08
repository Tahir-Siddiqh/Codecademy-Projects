# Different Businesses
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Franchise of the restraunt
class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

# Menu of the restraunt
class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name, str(self.start_time), str(self.end_time))

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total

# Brunch Menu
item1 = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu("brunch",item1,1100,1600)

# Early Bird Menu
item2 = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

early_bird = Menu("early bird", item2, 1500, 1800)

# Dinner Menu
item3 = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner = Menu("dinner", item3, 1700, 2300)

# Kids Menu
item4 = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids = Menu("kids", item4, 1100, 2100)

# Arepa's Menu
item5 = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Arepa", item5, 1000, 2000)

# All Diner Menus' togeather
menus = [brunch, early_bird, dinner, kids]

# Stores
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

# Businessess
business1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
business2 = Business("Take a' Arepa",[arepas_place])


# Tests for all the above code.

#print(brunch)
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))
