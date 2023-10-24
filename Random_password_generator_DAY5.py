import random
print("""
\t  /\_/\  
\t ( o.o )
Password Generator Project
\t (  -  )
\t  > ^ <
""")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
stage = input(" Do you prefer a robust or a less secure encryption? Type 'robust' or 'less' -> .\n")

password = ""
loops = []
if stage == "less":
  for char in range(1,nr_letters +1):
    password += random.choice(letters)
  
  for char in range(1, nr_symbols+ 1):
    password += random.choice(symbols)
  
  for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
    
else:
  for char in range(1,nr_letters +1):
    loops  += random.choice(letters)

  for char in range(1, nr_symbols+ 1):
    loops+= random.choice(symbols)

  for char in range(1,nr_numbers+1):
    loops += random.choice(numbers)

random.shuffle(loops)

for i in range (0,len(loops)):
  password += loops[i]

print("Your password is: ", password)

