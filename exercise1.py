from decimal import Decimal
from time import sleep
# Data types

#Text - Unicode Strings
simple_string = "This is regular text, the kind you can represent with the ABCs. (ASCII)"
print(simple_string)
input()

not_so_simple_string = "美国人看不懂。"
print(not_so_simple_string)
input()

fun_string = "You can also use emojis 😂🥨🍄🍌."
print(fun_string)
input()

# You'll use this in most cases. We will look at other types of strings in a later session.


#Numbers - Tricky, Tricky

# Integers
value_z = 1
value_y = 2
print(value_z + value_y)
input()
# Decimal Like - Float
value_a = 1.0
value_b = 0.9

# Floats are tricky...
print('Basic math right?')
input()
print(value_a - value_b)
input()
# Convertinga float to a decimal creates a super precise float by default
value_c = Decimal(value_a)
value_d = Decimal(value_b)

print('Will the result be 0.1?')
input()
print(value_c - value_d)

# Converting a float to a string 
value_e = Decimal(str(value_a))
value_f = Decimal(str(value_b))

print('Will 1.0 - 0.9  finally equal 0.1?')
input()
print(value_e - value_f)

# Array like things
stuff = ['Ronnie', 'Bobby', 'Ricky', 'Mike']
more_stuff = ('Tito, Michael, Randy')

# The difference is  You can modify a list but not a tuple
stuff.append('Ralph')
print(stuff)
input()
# This could fail more_stuff.append('Janet')

#Dictionaries - an unordered list of items that stores a value by a name (key/pair)


