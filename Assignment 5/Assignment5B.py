import random
def initializeDB(my_db):
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for i in range(rows):
        list = []
        for j in range(columns):
            if random.randint(0, 100) / 100 >= 0.7:
                list.append("R")
            else:
                list.append("A")
        my_db.append(list)
def displayDBFancy(my_db):
    for i in range(len(my_db)):
        for j in my_db[i]:
            print(f"{j}", end=" ")
        print()
def getAvailibleSeats(my_db):
    count = 0
    for i in range(len(my_db)):
        for j in my_db[i]:
            if j == "A":
                count += 1

    return count
def main():
    my_db = []
    initializeDB(my_db)
    print(f"Number of available seats: {getAvailibleSeats(my_db)}")
    displayDBFancy(my_db)

    while(getAvailibleSeats(my_db) != 0):
        my_tuple = (int(input(f"Enter the row number (0 to {len(my_db) - 1}): "))
                    ,int(input(f"Enter the column number (0 to {len(my_db[0]) - 1}): "))
                    )

        if my_db[my_tuple[0]][my_tuple[1]] == "A":
            my_db[my_tuple[0]][my_tuple[1]] = "B"
            print("Seat booked successfully!")
        else:
            print("This seat has already been booked.")

        displayDBFancy(my_db)

    print("All available seats have been booked!")
    displayDBFancy(my_db)

if __name__ == "__main__":
    main()