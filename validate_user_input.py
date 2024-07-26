username=input("enter a username : ")
username.find(" ")
username.isalpha()
if len(username) > 12 :
  print("your username can't be more than 12 character")
elif not  username.find(" ") == -1:
  print("your username can't contain  spaces")
elif not username.isalpha():
  print("your username can't contain numbers")
else: 
  print(f"welcome {username}")