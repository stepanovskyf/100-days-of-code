import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
string_letters = ""
string_numbers = ""
string_symbols = ""
end_string = ""
for item in range(0, nr_letters):
    random_letter = random.choice(letters)
    string_letters = string_letters + random_letter
for item in range(0, nr_numbers):
    random_number = random.choice(numbers)
    string_numbers = string_numbers + random_number
for item in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    string_symbols = string_symbols + random_symbol
password = string_letters + string_numbers + string_symbols
password_list = []
for letter in password:
    password_list.append(letter)
random.shuffle(password_list)
for item in password_list:
    end_string += item
print(end_string)
