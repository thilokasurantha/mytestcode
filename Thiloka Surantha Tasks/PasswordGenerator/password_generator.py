import random

lower_letters = "abcdefghijlkmnopqrstuvwxyz"
upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+"

upper = random.choice(lower_letters)+random.choice(lower_letters)+random.choice(lower_letters)+random.choice(lower_letters)+random.choice(lower_letters)
num = random.choice(numbers)+random.choice(numbers)
symbol = random.choice(symbols)+random.choice(symbols)+random.choice(symbols)+random.choice(symbols)+random.choice(symbols)
lower = random.choice(upper_letter)+random.choice(upper_letter)+random.choice(upper_letter)+random.choice(upper_letter)+random.choice(upper_letter)
anum = random.choice(numbers)+random.choice(numbers)+random.choice(numbers)+random.choice(numbers)

print("Password Generated : ", upper+num+symbol+lower+anum)