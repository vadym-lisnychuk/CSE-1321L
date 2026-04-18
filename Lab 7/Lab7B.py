import MyMath

def main():
    number_1 = int(input("Enter number 1: "))
    number_2 = int(input("Enter number 2: "))

    print(f"Min is {MyMath.my_min(number_1, number_2)}")
    print(f"Max is {MyMath.my_max(number_1, number_2)}")
    print(f"Average is {MyMath.my_avg(number_1, number_2)}")


if __name__ == "__main__":
    main()