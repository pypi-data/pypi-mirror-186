def mat_add():
    rows = int(input('ENter number of rows: '))
    cols = int(input('ENter number of column: '))

    print()  # for new line
    print('Enter values for matrix A')

    matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                 for j in range(cols)] for i in range(rows)]

    print()  # for new line
    print('Enter values for matrix B ')

    matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                 for j in range(cols)] for i in range(rows)]

    print()  # for new line

    print('Matrix-A :')
    for i in matrix_A:
        print(i)

    print()  # for new line

    print('Matrix-B :')
    for i in matrix_B:
        print(i)

# resultant matrix (matrix that store answer and intially it is Zero)
    result = [[0 for j in range(cols)] for i in range(rows)]

# addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] + matrix_B[i][j]

    print()  # for new line
    print('Addition of Matrix-A and Matrix-B is :')

    for i in result:
        print(i)

# matrix subtraction in python


def mat_sub():

    rows = int(input('ENter number of rows: '))
    cols = int(input('ENter number of column: '))

    print()  # for new line

    print('Enter values for matrix A')
    matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                 for j in range(cols)] for i in range(rows)]

    print()  # for new line

    print('Enter values for matrix B ')
    matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                 for j in range(cols)] for i in range(rows)]

    print()  # for new line

    print('Matrix-A :')
    for i in matrix_A:
        print(i)

    print()  # for new line

    print('Matrix-B :')
    for i in matrix_B:
        print(i)

# resultant matrix (matrix that store answer and intially it is Zero)
    result = [[0 for j in range(cols)] for i in range(rows)]

# subtraction
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] - matrix_B[i][j]

    print()  # for new line

    print('Subtraction of Matrix-A and Matrix-B is :')
    for i in result:
        print(i)

# matrix multiplication in python


def mat_mul():
    matrix_A_rows = int(input('ENter number of rows for matrix-A: '))
    matrix_A_cols = int(input('ENter number of columns for matrix-A: '))

    print()  # for new line

    matrix_B_rows = int(input('ENter number of rows for matrix-B: '))
    matrix_B_cols = int(input('ENter number of columns for matrix-B: '))

    print()  # for new line

    if matrix_A_cols == matrix_B_rows:
        print('Enter values for matrix A')
        matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                     for j in range(matrix_A_cols)] for i in range(matrix_A_rows)]

        print()  # for new line

        print('Enter values for matrix B ')
        matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:"))
                     for j in range(matrix_B_cols)] for i in range(matrix_B_rows)]

        print()  # for new line

        print('Matrix-A :')
        for i in matrix_A:
            print(i)

        print()  # for new line

        print('Matrix-B :')
        for i in matrix_B:
            print(i)

    # mutiplication operation

    # resultant matrix (matrix that store answer and intially it is Zero)
        result = [[0 for j in range(matrix_B_cols)]
                  for i in range(matrix_A_rows)]

    # main logic for matrix multiplication (multiplication operation)
        for i in range(len(matrix_A)):
            for j in range(len(matrix_B[0])):
                for k in range(len(matrix_B)):
                    result[i][j] += matrix_A[i][k] * matrix_B[k][j]

        print()  # for new line

        print('Multiplication of Matrix-A and Matrix-B is :')
        for i in result:  # print result
            print(i)

    else:
        print('Multiplication of matrices is not possible (columns of matrix-A = row of matrix-B)')


# matrix transpose

def mat_trans():
    row = int(input('Enter number of row: '))
    col = int(input('Enter number of col: '))

#  create a matrix using input() function and nested list comprehension
    matrix = [[int(input(f'column {j+1} -> ENter {i+1} element:'))
               for j in range(col)] for i in range(row)]

# create another list where we store result (transpose of matrix)
    transpose = [[0 for i in range(row)] for j in range(col)]

    print()    # for new line

# print matrix
    print('matrix: ')
    for i in matrix:
        print(i)

# transpose of matrix
    for i in range(row):
        for j in range(col):
            transpose[j][i] = matrix[i][j]

    print()   # new line

# print transpose of matrix
    print('Transpose of matrix: ')
    for i in transpose:
        print(i)
