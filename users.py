import database
import sys   # Import the sys module to use sys.exit() for exiting the program


# Function to display user details and show the user menu
def welcome_user(connection, accountid):
    # Fetch user details from the database using the account ID
    user_details = database.get_user_details(connection, accountid)
    if user_details:
        print("\nYour Account Details:")
        print(f"\tAccount ID: {user_details[0]}")
        print(f"\tUsername: {user_details[1]}")
        print(f"\tID: {user_details[2]}")
        print(f"\tEmail: {user_details[3]}")
        print(f"\tBalance: Ksh {user_details[5]:.2f}")
        
        # Call the user menu to show options after displaying details
        user_menu(connection, accountid)
        
    else:
        print("Unable to retrieve user details.")


# Function to display the user menu and handle user choices
def user_menu(connection, accountid):
    while True:
        print("\n\nHOW WOULD YOU LIKE TO PROCEED?")
        print("\t1. DEPOSIT INTO ACCOUNT")
        print("\t2. WITHDRAW FROM ACCOUNT")
        print("\t3. SEND MONEY TO DIFFERENT ACCOUNT")
        print("\t4. LOG OUT")
        
        choice = input("ENTER YOUR CHOICE(1-4): ")
        
        if choice == "1":
            deposit(connection, accountid)
        elif choice == "2":
            withdraw(connection, accountid)
        elif choice == "3":
            send_money(connection, accountid)
        elif choice == "4":
            logout_user()
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
        


def deposit(connection, accountid):
    amount = float(input("\nEnter the amount to deposit(Ksh): "))
    user_details = database.get_user_details(connection, accountid)   # Fetch user details from the database
    
    new_balance = user_details[5] + amount

    database.update_balance(connection, accountid, new_balance)   # Update the balance in the database
    print(f"\nDeposit successful! New balance: Ksh {new_balance:.2f}")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\nWOULD YOU LIKE TO PROCEED? (Y/N)")
    
    choice = input("ENTER YOUR CHOICE: ")
    
    
    if choice == "Y" or choice == "y":
        user_menu(connection, accountid)
    elif choice == "N" or choice == "n":
        logout_user()
    else:
        print("INVALID CHOICE")
    
    
def withdraw(connection, accountid):
    amount = float(input("Enter the amount to withdraw: "))
    user_details = database.get_user_details(connection, accountid)  # Fetch user details from the database
    
     # Check if the withdrawal amount is more than the available balance
    if amount > user_details[5]:
        print("Insufficient funds. Withdrawal amount exceeds available balance.")
    else:
        new_balance = user_details[5] - amount
        database.update_balance(connection, accountid, new_balance)# Update the balance in the database
        print(f"Withdrawal successful! New balance: Ksh {new_balance:.2f}")
    
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\nWOULD YOU LIKE TO PROCEED? (Y/N)")
    
    choice = input("ENTER YOUR CHOICE: ")
    
    
    if choice == "Y" or choice == "y":
        user_menu(connection, accountid)
    elif choice == "N" or choice == "n":
        logout_user()
    else:
        print("INVALID CHOICE")



def send_money(connection, sender_accountid):
    recipient_accountid = input("Enter the recipient's account ID: ")
    recipient_details = database.get_user_details(connection, recipient_accountid)  # Fetch recipient details from the database
    
    # Check if the recipient's account exists
    if recipient_details:
        # Check if the recipient's account exists
        print("\n---------Recipient's Account Details: -------------")
        print(f"\tAccount ID: {recipient_details[0]}")
        print(f"\tUsername: {recipient_details[1]}")
        print(f"\tID: {recipient_details[2]}")
        print(f"\tEmail: {recipient_details[3]}")
        print("------------------------------------------------------")
        
        amount = float(input("\nEnter the amount to send (Ksh): "))
        sender_details = database.get_user_details(connection, sender_accountid)# Fetch sender's details from the database
        
        # Check if the sender has enough funds for the transfer
        if amount > sender_details[5]:
            print(f"Insufficient funds. Transfer amount exceeds available balance. You have Ksh {sender_details[5]} available.")
        else:
            # Calculate new balances for both the sender and recipient
            new_sender_balance = sender_details[5] - amount
            new_recipient_balance = recipient_details[5] + amount
            
            # Update the balances in the database
            database.update_balance(connection, sender_accountid, new_sender_balance)
            database.update_balance(connection, recipient_accountid, new_recipient_balance)
            
            print(f"\nTransfer successful! New balance: Ksh {new_sender_balance:.2f}")
            #print(f"Recipient's new balance: ${new_recipient_balance:.2f}")
    else:
        print("Recipient account does not exist.")
    
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\nWOULD YOU LIKE TO PROCEED? (Y/N)")
    
    choice = input("ENTER YOUR CHOICE: ")
    
    
    if choice == "Y" or choice == "y":
        user_menu(connection,sender_accountid)
    elif choice == "N" or choice == "n":
        logout_user()
    else:
        print("INVALID CHOICE")


def logout_user():
    print("\nThank you for banking with us. Have a nice day!")
    print("------------------------------------------------------------------------------------------------------------------------------")
    sys.exit()






connection = database.connect()