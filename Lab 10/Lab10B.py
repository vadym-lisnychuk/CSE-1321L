def menu(logged_in):
    print("Choose an option")
    if logged_in:
        print("3 - Change Password")
        print("4 - Logout")
    else:
        print("1 - Login")
        print("2 - Register")
    print("E - Exit")
    return input()

def main():
    my_db = {}
    logged_in = False
    while True:
        print()
        match menu(logged_in):
            case "1":
                print("[Login]")
                username = input("Username: ")
                password = input("Password: ")
                if username in my_db and my_db[username] == password:
                        print("Success!")
                        logged_in = True
                else:
                    print("Incorrect username/password!")

            case "2":
                print("[Register]")
                username = input("Username: ")
                password = input("Password: ")
                my_db[username] = password
                print("User successfully added!")
            case "3":
                print("\n[Changin password]")
                my_db[username] = input("Password: ")
            case "4":
                print("\nLogging Out...")
                logged_in = False
            case "E":
                break

if __name__ == "__main__":
    main()