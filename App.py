import random
length=int(input())

numbers="0123456789"
characters="@#%&-+()?!;:*,_/^={}\[]"
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password=""

while(len(password)<length):
 password_formula=[random.choice(numbers),random.choice(characters),random.choice(lowercase),random.choice(uppercase)]
 password+=random.choice(password_formula)

print(f"Generated {length} symbols strong password :\n")
print(password)
