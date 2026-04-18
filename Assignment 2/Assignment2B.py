print("[Owl World]")

username = ""
password = ""

option = 0
account = False

while (option != 3):
    if account:
        adult_price = 22.00
        children_price = 18.00
    else:
        adult_price = 28.00
        children_price = 24.00
    #menu
    if account:
        print(f"Welcome {username}!")
    
    print("Choose an option:")
    print("1. Buy Tickets")

    if account:
        print("2. Sign Out")
    else:
        print("2. My Account")

    print("3. Exit")
    option = int(input("> "))
    print()

    if option == 1:
        print("Ticket Prices:")
        print(f"Adult: ${adult_price:.2f}, Children: ${children_price:.2f}")
        print("")

        adult_tickets_count = int(input("How many Adult tickets?: "))
        child_tickets_count = int(input("How many Children tickets?: "))

        print("\nProcessing...\n")
        print(f"{adult_tickets_count}x Adult Tickets ---- ${(adult_price * adult_tickets_count):.2f}")
        print(f"{child_tickets_count}x Children Tickets ---- ${(children_price * child_tickets_count):.2f}")
        print(f"Total: ${(adult_price * adult_tickets_count + children_price * child_tickets_count):.2f}")
        print()
    elif option == 2:
        if account:
            account = False
        else:
            print("Choose an option:")
            print("1. Sign-in")
            print("2. Register")
            account_option = int(input("> "))

            match account_option:
                case 1:
                    input_username = input("Username: ")
                    input_password = input("Password: ")

                    if(input_username == username and input_password == password):
                        account = True
                        print("Login Successful!")
                        print()

                    else:
                        print("Incorrect Username/Password")
                        print()
                case 2:
                    username = input("Username: ")
                    password = input("Password: ")
                    print("Registration Successful!")
                    print()

print("Program Terminated")