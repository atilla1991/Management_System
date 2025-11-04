import os #To handle file paths and directories
from datetime import datetime #To write log dates and times

#To print main menu and continue to next menu(Ayşenur)
def main_menu():
    print("\n----Main Menu----")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Quit")
    selection = input("Please select an option: ")
    return selection

#To login as a user and check for password and username(Ayşenur)
def user_login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    try:
        with open("PMS/users.txt", "r",encoding="utf8") as user:
            for line in user:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_username, correct_password = parts
                    if username == correct_username and password == correct_password:
                        add_log_entry(username)
                        clear_terminal()
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'PMS/users.txt' file not found")

#To login as a admin and check for password and usernmae(Ayşenur)
def admin_login():
    username=input("Enter your username: ")
    password= input("Enter your password: ")
    try:
        with open("PMS/admins.txt", "r",encoding="utf8") as admin:
            for line in admin:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_admin_username, correct_admin_password = parts
                    if username == correct_admin_username and password == correct_admin_password:
                        add_log_entry(username)
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'PMS/admins.txt' file not found")

#To quit seesion for both user and admin(Ayşenur)
def quit_session(username):
    if username:
        print(f"----{username} has logged out successfully.----")
    else:
        print("Quitting the program. Goodbye!")

#To add log entry when user or admin logs in(Kadir)
def add_log_entry(username):
    with open("PMS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged in.\n")

#To add log entry when user or admin logs out(Kadir)
def add_logout_entry(username):
    with open("PMS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged out.\n")

#To list logs and reset them as admin(Kadir)
def list_and_reset_logs(username):
    clear_terminal()
    print("\n--- System Logs ---")
    try:
        with open("PMS/logs.txt", "r", encoding="utf8") as file:
            logs = file.readlines()
            if not logs:
                print("No log entries found.")
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("Log file not found.")
    
    reset_choice = input("\nDo you want to reset the logs? (y/n): ")
    if reset_choice.lower() == 'y':
        with open("PMS/logs.txt", "w", encoding="utf8") as file:
            file.write("")
            file.write(f"Logs have been reseted by {username}.\n")
        print("System logs have been reset.")

#To add or remove products as user(Atilla)
def add_or_remove_product():
    product_name = input("Enter product name: ").lower()

    try:
        change = int(input("Enter a positive number to add stock, a negative number to remove: "))
    except ValueError:
        print("Invalid number entered.")
        return

    products = {}
    try:
        with open("PMS/products.txt", "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, quantity = line.split("-", 1)
                    products[name.strip()] = int(quantity.strip())
                except ValueError:
                    continue
    except FileNotFoundError:
        open("PMS/products.txt", "w", encoding="utf8").close()

    current_stock = products.get(product_name, 0)
    new_stock = current_stock + change
    
    if product_name not in products and change <= 0:
        print("Product does not exist, cannot remove stock.")
        return
    if new_stock < 0:
        print(f"Not enough stock to remove. Current stock: {current_stock}")
        return
        
    products[product_name] = new_stock
    
    with open("PMS/products.txt", "w", encoding="utf8") as file:
        for name, quantity in products.items():
            if quantity > 0:
                file.write(f"{name}-{quantity}\n")

    if change > 0:
        print(f"{change} units added to '{product_name}'. New stock: {new_stock}")
    elif change < 0:
        print(f"{abs(change)} units removed from '{product_name}'. New stock: {new_stock}")
    else:
        print("No change in stock was made.")

    if new_stock == 0:
        print(f"Stock for '{product_name}' is now zero and it has been removed from the list.")

#To list products as user(Atilla)
def list_products():
    clear_terminal()
    print("\n--- Product List ---")
    try:
        with open("PMS/Products.txt", "r", encoding="utf8") as file:
            products = file.readlines()
            if not products:
                print("No products found.")
            for product in products:
                print(product.strip())
    except FileNotFoundError:
        print("No products have been added yet.")

#To clear terminal screen(Atilla)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

