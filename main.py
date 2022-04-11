#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
l=""
for le in letters:
  if len(l)<nr_letters:
     le=random.randint(0,len(letters)-1)
     l+=letters[le]
s=""
for sy in symbols:
  if len(s)<nr_symbols:
    sy=random.randint(0,len(symbols)-1)
    s+=symbols[sy]
n=""
for nu in numbers:
  if len(n)<nr_numbers:
    nu=random.randint(0,len(numbers)-1)
    n+=numbers[nu]
password=l+s+n
password_as=list(password)
random.shuffle(password_as)
final_password=''.join(password_as)
print(f"{final_password}")

  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P