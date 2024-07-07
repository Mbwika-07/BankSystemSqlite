import database
import users
import admins

def login_user(connection):
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tLOG INTO ACCOUNT")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    
    accountid = input("Enter your account id: ")
    password = input("Enter your password: ")
        
    userdet = database.verify_user(connection, accountid, password)
        
    if userdet:
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"\t\t\t\t\t\tWELCOME BACK {userdet[1].upper()} !")
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        users.welcome_user(connection, accountid)
    else:
        print("Invalid username or password. Please try again.")



def signup_newuser(connection):
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tCREATE NEW ACCOUNT")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    
    username = input("Enter your username: ")
    id = input("Enter you national ID number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    database.add_user(connection, username, id, email, password, 0.0)
    
    print("Account created successfully. Try to log in later as the admin has to approve your account.")


def login_admin(connection):
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tLOG IN AS ADMINISTRATOR ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    
    id = input("Enter your account id: ")
    password = input("Enter your password: ")
        
    userdet = database.verify_admin(connection, id, password)
        
    if userdet:
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"\t\t\t\t\t\tWELCOME TO THE ADMIN DASHBOARD {userdet[1].upper()} !")
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        admins.welcome_admin(connection, id)
    else:
        print("Invalid username or password. Please try again.")








def main():
    is_running = True
    connection = database.connect()

    while is_running == True:
        print("\n\n-------------------------------NATIONAL BANK------------------------------------")
        print("WELCOME TO THE NATIONAL BANK PROGRAM. HOW WOULD YOU LIKE TO PROCEED?")
        print("\t1. CUSTOMER LOGIN PAGE")
        print("\t2. ADMIN LOGIN PAGE")
        print("\t3. SIGN IN NEW USER.")
        print("\t4. EXIT")
        choice = input("KINDLY ENTER YOUR CHOICE(1-4): ")
        
        if choice == "1":
            login_user(connection)
        elif choice == "2":
            login_admin(connection)
        elif choice == "3":
            signup_newuser(connection)
        elif choice == "4":
            is_running = False
        else:
            print("INVALID CHOICE")

if __name__ == "__main__":
    main()