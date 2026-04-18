class Todo:
    def __init__(self, title, date = None, time = None):
        self.title = title
        self.date = date
        self.time = time
        self.done = False
    def set_done(self):
        self.done = True
    def is_done(self):
        return self.done
    def set_date_time(self, date, time):
        self.date = date
        self.time = time
    def has_due_dt(self):
        return self.time != None and self.date != None
    def get_todo(self):
        my_string = f"{self.title}"
        if self.has_due_dt():
            my_string += f"\n\t Due: {self.date} at {self.time}"
        return my_string

#main menu returns user choice
def menu():
    print("1 - Add a To-do list item")
    print("2 - Set a To-do list item as done")
    print("3 - Set or change the due date time of a To-do item")
    print("4 - Remove a To-do list item due date and time")
    print("5 - Print To-do list")
    print("6 - Exit")
    return int(input("> "))

# option 1
def add(my_db):
    has_date_time = input("Does your To-do item have a due date and time? (y/n): ")
    title = input("What is the title: ")

    if has_date_time == 'y':
        date = input("Enter the due date (MM/DD/YYYY): ")
        time = input("Enter the due time (HH:MM AM/PM): ")
        temp = Todo(title, date, time)
    else:
        temp = Todo(title)

    print("Adding your To-do list item...")
    my_db.append(temp)

#shows minial list to append some field, for options 2, 3, etc.
def minimal_viewer(my_db):
    for i in range(len(my_db)):
        print(f"{i} {my_db[i].title}")
    return int(input("> "))

#option 2
def set_done_db(my_db):
    print("Choose a To-do item to set or change due date time: ")

    for i in range(len(my_db)):
        print(f"{i} {my_db[i].title}")

    idx = int(input("> "))
    my_db[idx].set_done()

#option 3
def change_due_date_db(my_db):
    print("Choose a To-do item to set or change due date time: ")

    for i in range(len(my_db)):
        print(f"{i} {my_db[i].title}")
    idx = int(input("> "))
    date = input("Enter the due date (MM/DD/YYYY): ")
    time = input("Enter the due time (HH:MM AM/PM): ")

    my_db[idx].set_date_time(date, time)

#option 4
def remove(my_db):
    print("Choose a To-do item to remove its due date time:")

    for i in range(len(my_db)):
        if my_db[i].has_due_dt():
            print(f"{i} {my_db[i].title}")

    idx = int(input("> "))
    my_db[idx].set_date_time(None, None)

def show(my_db):
    print("This is your To-do list: ")
    for event in my_db:
        if not event.done:
            print(f"- {event.get_todo()}")

def main():
    my_db = []
    while True:
        match menu():
            case 1:
                add(my_db)
            case 2:
                set_done_db(my_db)
            case 3:
                change_due_date_db(my_db)
            case 4:
                remove(my_db)
            case 5:
                show(my_db)
            case 6:
                print("[Terminating program...]")
                break
            case _:
                pass
        print()
if __name__ == "__main__":
    main()