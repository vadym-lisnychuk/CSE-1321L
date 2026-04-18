print("[Mailing List]")

def menu():
    print()
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    temp = input("Make your selection: ")
    print()
    return temp

def main():
    myList = []
    while True:
        match menu():
            case "1":
                myList.append(input("Enter the email to be added: "))
                print("Email added to mailing list.")
            case "2":
                temp = input("Enter the email to be removed: ")
                if temp in myList:
                    myList.remove(temp)
                    print(f"{temp} has been removed from the mailing list.")
                else:
                    print(f"No such email in mailing list: {temp}")
            case "3":
                for i in myList:
                    print(i)
            case "4":
                print("Shutting down...")
                break
            case _:
                pass

if __name__ == "__main__":
    main()