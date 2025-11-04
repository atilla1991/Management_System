import functions #Importing functions module
import os #To handle file paths and directories
os.makedirs("PMS", exist_ok=True) #Check PMS directory exists

while True:
    choice = functions.main_menu() #Main Menu
    if choice == "1":# User Login
        username = functions.user_login()
        if username:# User logged in successfully
            while True:# User Panel
                print("\n--- User Panel  ---")
                print("1. Add or Remove Product Stock")
                print("2. List Products")
                print("3. Logout to Main Menu")
                user_choice = input("Please choose an option: ")

                if user_choice == "1":#add or remove product stock
                    functions.add_or_remove_product()
                elif user_choice == "2":#list products
                    functions.list_products()
                elif user_choice == "3":# Logout to Main Menu
                    functions.clear_terminal()
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break

    elif choice == "2": # Admin Login
        username = functions.admin_login()
        if username:# Admin logged in successfully
            while True:# Admin Panel
                print("\n--- Admin Panel ---")
                print("1. List logs-reset logs")
                print("2. Add New User")
                print("3. List Users")
                print("4. Remove User")
                print("10. Logout to Main Menu")
                admin_choice = input("Please choose an option: ")

                if admin_choice == "1":#Log list and reset
                    functions.list_and_reset_logs(username)
                elif admin_choice == "2":#To add new user as admin
                    functions.add_new_user
                elif admin_choice == "3":#To list users as admin
                    functions.list_users()
                elif admin_choice == "4":#To remove user as admin
                    functions.list_users()
                    functions.remove_users()
                elif admin_choice == "10":# Logout to Main Menu
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break

    elif choice == "3": # Quit
        functions.clear_terminal()
        print("Quitting the program. Goodbye!")
        break

    else: # Invalid option
        print("Invalid option. Please try again.")