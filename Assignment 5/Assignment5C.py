class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.matrix = []
        for i in range(self.rows):
            row = [0] * self.cols
            self.matrix.append(row)

    def str_list_to_matrix(self, my_list):
        my_list = my_list.split(",")

        if len(my_list) != self.rows * self.cols:
            print("Invalid length list")

        k = 0
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(my_list[k])
                k += 1


    def show(self, name):
        print(f"Matrix {name}")
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end=" ")
            print()
        print()

    def get_column(self, j):
        col = []
        for row in self.matrix:
            col.append(row[j])
        return col

def matrix_multiplication(A, B):
        C = Matrix(A.rows, B.cols)
        for i in range(C.rows):
            for j in range(C.cols):
                C.matrix[i][j] = dot_product(A.matrix[i], B.get_column(j))

        return C

def dot_product(vector_a, vector_b):
    sum = 0
    for i in range(len(vector_b)):
        sum += vector_a[i] * vector_b[i]
    return sum

def main():
    rows_a = int(input("Enter rows for Matrix A: "))
    cols_a = int(input("Enter columns for Matrix A: "))
    print()

    rows_b = int(input("Enter rows for Matrix B: "))
    cols_b = int(input("Enter columns for Matrix B: "))
    print()

    if(rows_a != cols_b):
        print("Matrix multiplication is not possible.")
        print("Number of columns in Matrix A must equal number of rows in Matrix B.")
    else:
        A = Matrix(rows_a, cols_a)
        B = Matrix(rows_b, cols_b)

        str_a = input("Enter Matrix A values (comma-separated): ")
        str_b = input("Enter Matrix B values (comma-separated): ")
        print()

        A.str_list_to_matrix(str_a)
        B.str_list_to_matrix(str_b)

        A.show("A")
        B.show("B")
        matrix_multiplication(A, B).show("Resulting Matrix:")

if __name__ == "__main__":
    main()