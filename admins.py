import database

def welcome_admin(connection, id):
    # Fetch admin details from the database using the admin ID
    admin_details = database.get_admin_details(connection, id)
    
    if admin_details:
        print("\nYour Account Details:")
        print(f"\tAccount ID: {admin_details[0]}")
        print(f"\tUsername: {admin_details[1].title()}")
        
        # Call the admin menu to show options after displaying details
        admin_menu(connection)
    else:
        print("Unable to retrieve admin details.")

def admin_menu(connection):
    while True:
        print("\n\nHOW WOULD YOU LIKE TO PROCEED?")
        print("\t1. SEARCH USERS ACCOUNT BY NAME")
        print("\t2. APPROVE USERS")
        print("\t3. CHANGE USER PASSWORD")
        print("\t4. DELETE USER ACCOUNT")
        print("\t5. LOG OUT")
        
        choice = input("ENTER YOUR CHOICE(1-5): ")
        
        if choice == "1":
            search_user()
        elif choice == "2":
            approve_users(connection)  # Pass only the connection
        elif choice == "3":
            change_password()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            logout_admin()
            break
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")


def approve_users(connection):
    new_users = database.select_new_users(connection)
    
    for user in new_users:
        username, id, email, password, balance = user
        print("\nNew User Details:")
        print(f"\tUsername: {username}")
        print(f"\tID: {id}")
        print(f"\tEmail: {email}")
        print(f"\tBalance: {balance}")
        
        choice = input("Do you want to approve this user? (yes/no): ").strip().lower()
        
        if choice == "yes":
            database.add_user_to_usertable(connection, username, id, email, password, balance)
            print(f"User {username} approved and added to the users table.")
            database.delete_new_user(connection, username, id, email, password, balance)
            print(f"User {username} deleted from the new_users table.")
        elif choice == "no":
            print(f"User {username} was not approved and remains in the new_users table.")
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
    
    print("\nAll new users have been processed.")

def logout_admin():
    print("Logging out...")
    exit()

def search_user():
    pass

def change_password():
    pass

def delete_user():
    pass
