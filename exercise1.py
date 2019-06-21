from decimal import Decimal
# Data types

#Text - Unicode Strings
simple_string = "This is regular text, the kind you can represent with the ABCs. (ASCII)"
print(simple_string)

not_so_simple_string = "美国人看不懂。"
print(not_so_simple_string)

fun_string = "You can also use emojis 😂🥨🍄🍌."
print(fun_string)

# You'll use this in most cases. We will look at other types of strings in a later session.


#Numbers - Tricky, Tricky

# Integers
value_z = 1
value_y = 2
print(value_z + value_y)

# Decimal Like - Float
value_a = 1.0
value_b = 0.9

# FLoats are tricky...
print(value_a - value_b)

# Convertinga float to a decimal creates a super precise float by default
value_c = Decimal(value_a)
value_d = Decimal(value_b)

print(value_c - value_d)

# Converting a float to a string 
value_e = Decimal(str(value_a))
value_f = Decimal(str(value_b))

print(value_e - value_f)
