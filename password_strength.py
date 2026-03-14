import re

password = input("Enter your password: ")

has_letter = re.search("[a-zA-Z]", password)
has_number = re.search("[0-9]", password)
has_special = re.search("[@#$%^&*!]", password)

if has_letter and has_number and has_special and len(password) >= 8:
    print("Strong Password")

elif (has_letter and has_number) or (has_letter and has_special) or (has_number and has_special):
    print("Moderate Password")

else:
    print("Low Strength Password")