import database

def welcome_admin(connection, id):
    # Fetch user details from the database using the account ID
    admin_details = database.get_admin_details(connection, id)
    
    if admin_details:
        print("\nYour Account Details:")
        print(f"\tAccount ID: {admin_details[0]}")
        print(f"\tUsername: {admin_details[1].title()}")
        
        # Call the user menu to show options after displaying details
        admin_menu(connection, id)
        
    else:
        print("Unable to retrieve user details.")


def admin_menu(connection, id):
    while True:
        print("\n\nHOW WOULD YOU LIKE TO PROCEED?")
        print("\t1. SEARCH USERS ACCOUNT BY NAME")
        print("\t2. APPROVE USERS")
        print("\t3. CHANGE USER PASSWORD ")
        print("\t4. DELETE USER ACCOUNT")
        print("\t5. LOG OUT")
        
        choice = input("ENTER YOUR CHOICE(1-4): ")
        
        if choice == "1":
            search_user(connection, id)
        elif choice == "2":
            approve_users(connection, id)
        elif choice == "3":
            change_password(connection, id)
        elif choice == "4":
            delete_user(connection, id)
        elif choice == "5":
            logout_admin()
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
            

def search_user():
    pass

def approve_users():
    pass

def change_password():
    pass

def delete_user():
    pass

def logout_admin():
    pass