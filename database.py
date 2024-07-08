import sqlite3


#CONNECTING THE DIFFERENT SQLITE QUERIES TO PYTHON VARIABLES
create_user_table_query = "CREATE TABLE IF NOT EXISTS users (accountid INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, id TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, balance REAL DEFAULT 0.0)"

create_admin_table_query = "CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)"

create_newuser_table_query = "CREATE TABLE IF NOT EXISTS new_users (username TEXT NOT NULL, id TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, balance REAL DEFAULT 0.0)"


check_user_credentials = "SELECT * FROM users WHERE accountid = ? AND password = ?;"

check_admin_credentials = "SELECT * FROM admins WHERE id = ? AND password = ?;"


insert_users = "INSERT INTO new_users (username, id, email, password, balance) VALUES (?, ?, ?, ?, ?);"
insert_admins = "INSERT INTO admins (username, password) VALUES (?, ?);"


get_user_details_query = "SELECT * FROM users WHERE accountid = ?;"
get_admin_details_query = "SELECT * FROM admins WHERE id = ?;"


update_balance_query = "UPDATE users SET balance = ? WHERE accountid = ?"

##query to transfer users from table new_uses to users
select_new_users_query = "SELECT * FROM new_users;"
insert_user_query = "INSERT INTO users (username, id, email, password, balance) VALUES (?, ?, ?, ?, ?);"
delete_new_user_query = "DELETE FROM new_users WHERE username = ? AND id = ? AND email = ? AND password = ? AND balance = ?;"



#TABLE DEFINITION FUNCTIONS
def connect():
    return sqlite3.connect("bank.db")

def create_table(connection):
    with connection:
        connection.execute(create_user_table_query)

def create_admin_table(connection):
    with connection:
        connection.execute(create_admin_table_query)

def create_newuser_table(connection):
    with connection:
        connection.execute(create_newuser_table_query)

#USERS FUNCTIONS
def verify_user(connection, username, password):
    with connection:
        return connection.execute(check_user_credentials, (username, password)).fetchone()

# def add_user(connection, username, id, email, password, balance):
#     with connection:
#         connection.execute(insert_users, (username, id, email, password, balance))

def get_user_details(connection, accountid):
    with connection:
        return connection.execute(get_user_details_query, (accountid,)).fetchone()

def update_balance(connection, accountid, new_balance):
    with connection:
        connection.execute(update_balance_query, (new_balance, accountid))




#ADMINS FUNCTIONS
def add_admin(connection, username, password):
    with connection:
        connection.execute(insert_admins, (username, password))#USED TO ADD A NEW ADMINISTRATOR

def verify_admin(connection, username, password):
    with connection:
        return connection.execute(check_admin_credentials, (username, password)).fetchone()

def get_admin_details(connection, id):
    with connection:
        return connection.execute(get_admin_details_query, (id,)).fetchone()


#NEW USER FUNCTIONS
def add_user(connection, username, id, email, password, balance=0.0):
    with connection:
        connection.execute(insert_users, (username, id, email, password, balance))

def select_new_users(connection):
    with connection:
        return connection.execute(select_new_users_query).fetchall()

def delete_new_user(connection, username, id, email, password, balance):
    with connection:
        connection.execute(delete_new_user_query, (username, id, email, password, balance))

def add_user_to_usertable(connection, username, id, email, password, balance=0.0):
    with connection:
        connection.execute(insert_user_query, (username, id, email, password, balance))





conn = connect()
create_table(conn)
create_admin_table(conn)
create_newuser_table(conn)
#add_user(conn, "testadmin", "123456789", "testadmin@example.com", "password", 0)
#add_admin(conn, "allan", "password")
conn.commit()