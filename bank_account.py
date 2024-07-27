
"""
  The Python script contains functions for a basic banking program allowing users to check balance,
  deposit, withdraw, and exit, with formatted display messages and input validation.
  
  :param balance: The `balance` parameter represents the current monetary balance in the account. It is used in functions like `withdrawl` to determine if there are sufficient funds for a withdrawal and in functions like `show_balance` to display the current balance to the user
  """
                                                                                                                                                                                                                                                                                                  
"""
  The function `show_balance` displays the balance in a formatted way.
  
  :param balance: The `show_balance` function takes a `balance` parameter, which is expected to be a
  numerical value representing a monetary balance. The function then prints out a formatted message
  displaying the balance with a currency symbol (€) and two decimal places
  """
  
def show_balance(balance):
  print("----------------------")
  print(f"your balance is €{balance:.2f}")
  print("----------------------")
  
"""
    The `deposit` function in Python prompts the user to enter an amount to be deposited and returns
    the amount if it is valid.
    :return: The function `deposit()` returns either the amount entered by the user if it is greater
    than or equal to 0, or 0 if the amount entered is less than 0.
    """
def deposit() :
  print("----------------------")
  amount = float(input("Enter an amout be deposited: € "))
  print("----------------------")
  
  if amount < 0:
    print("----------------------")
    print("That's not a valid amount")
    print("----------------------")
    return 0
  else:
    return amount


  """
  This Python function allows a user to withdraw a specified amount from their account balance,
  checking for sufficient funds and valid input.
  
  :param balance: The `balance` parameter in the `withdrawl` function represents the current balance
  in the account from which the withdrawal is being made. This balance is used to determine if the
  withdrawal amount requested by the user is within the available funds in the account
  :return: The function `withdrawl` returns the amount to be withdrawn if the conditions for
  withdrawal are met. If the amount is greater than the balance, it returns 0 with a message
  "Insufficient Balance". If the amount is less than 0, it returns 0 with a message "Amount must be
  greater than 0".
  """
def withdrawl(balance):
  print("----------------------")
  amount = float(input("Enter amount to be withdrawl : €"))
  print("----------------------")
  
  if amount > balance :
    print("----------------------")
    print("Insufficient Balance")
    print("----------------------")
    return 0
  elif amount < 0:
    print("----------------------")
    print("Amount must be greator than 0")
    print("----------------------")
    return 0
  else:
    return amount    

  """
  The main function allows users to perform banking operations such as checking balance, depositing,
  and withdrawing money, and exiting the program.
  """
def main():
  balance = 0
  is_running = True

  while is_running:
    print("----------------------")
    print("    Banking Program   ")
    print("----------------------")
    
    print("1. Show Balance")
    print("2. Deposit") 
    print("3. Withdraw") 
    print("4. Exit") 
    print("----------------------")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
      show_balance(balance)  
    elif choice == "2":
      balance += deposit()
    elif choice == "3":
      balance -= withdrawl(balance)
    elif choice =="4":
      is_running = False  
    else:
      print("----------------------")
      print("that is not a valid choice")
      print("----------------------")
      
    
  print("----------------------")
  print("Thank You! have a nice day!")
  print("----------------------")
  

# The `if __name__ == '__main__':` block in Python is used to check whether the current script is being run directly by the Python interpreter or if it is being imported as a module into another script.

if __name__ == '__main__':
  main()