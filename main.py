import database
import users

def login_user(connection):
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















def main():
    is_running = True
    connection = database.connect()

    while is_running == True:
        print("\n\n-------------------------------NATIONAL BANK------------------------------------")
        print("WELCOME TO THE NATIONAL BANK PROGRAM. HOW WOULD YOU LIKE TO PROCEED?")
        print("\t1. CUSTOMER LOGIN PAGE")
        print("\t2. ADMIN LOGIN PAGE")
        print("\t3. EXIT")
        choice = input("KINDLY ENTER YOUR CHOICE(1-3): ")
        
        if choice == "1":
            login_user(connection)
        elif choice == "2":
            pass
        elif choice == "3":
            is_running = False
        else:
            print("INVALID CHOICE")

if __name__ == "__main__":
    main()