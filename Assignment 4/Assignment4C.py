def Display_Main_Menu():
    print("ATM Main Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    return input("Please choose an option (1-4): ")

def Deposit(balance):
    add = float(input("Enter the amount to deposit: $"))
    print(f"Deposited ${add}. New balance: ${balance + add}\n")
    return balance + add

def Withdraw(balance):
    temp = float(input("Enter the amount to withdraw: $"))
    print(f"Withdrew ${temp}. New balance: ${balance}\n")
    return balance - temp

def Check_balance(balance):
    print(f"Your current balance is: ${balance}\n")



def main():
    print("Welcome to the ATM!")
    username = input("Please enter your name: ")
    balance = float(input("Enter your initial balance: $"))

    while True:
        match Display_Main_Menu():
            case '1':
                balance = Deposit(balance)
            case '2':
                balance = Withdraw(balance)
            case '3':
                Check_balance(balance)
            case '4':
                print(f"Goodbye, {username}! Thank you for using the ATM.")
                break
            case _:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

