credit_card = "1234-5678-2468-1357"
credit_card = credit_card[::-1]

print(credit_card[::3])
print(credit_card[-4:])


last_digit = credit_card[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")



#email slicing 

email = input("enter your email :")
index = email.index("@")
username = email[:index]
domain = email[index+1:]

print(f"your username is {username} and domain is {domain}")
