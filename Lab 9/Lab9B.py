print("[Friend List]")

def menu():
    print()
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    return input("Make your selection: ")


def main():
    myFriends = []
    while True:
        match menu():
            case "1":
                myFriends.append(
                                (
                                 input("Enter your friend's name: "),
                                 input("Enter your friend's age: ")
                                )
                                )
                print("Friend added")
            case "2":
                print()
                for i in myFriends:
                    print(f"Name: {i[0]}, Age: {i[1]}")

            case "3":
                print()
                print("Shutting down...")
                break

if __name__ == "__main__":
    main()