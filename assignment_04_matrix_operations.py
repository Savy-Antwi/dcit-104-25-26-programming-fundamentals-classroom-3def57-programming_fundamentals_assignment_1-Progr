# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i+1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix
 
def print_matrix(matrix):
    for row in matrix:
        print(row)
 
# Part A - Transpose
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
 
# Part B - Add two matrices
def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result
 
# Part C - Multiply two matrices
def multiply_matrices(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = [[0 for i in range(p)] for j in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + a[i][k] * b[k][j]
            result[i][j] = total
    return result
 
 
print("MATRIX OPERATIONS")
print("1. Transpose a Matrix")
print("2. Add Two Matrices")
print("3. Multiply Two Matrices")
choice = input("Choose an option (1-3): ")
 
if choice == "1":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print("Original Matrix:")
    print_matrix(matrix)
    print("Transposed Matrix:")
    print_matrix(transpose(matrix))
 
elif choice == "2":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Matrix A:")
    a = read_matrix(rows, cols)
    print("Matrix B:")
    b = read_matrix(rows, cols)
    print("A + B:")
    print_matrix(add_matrices(a, b))
 
elif choice == "3":
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of A / rows of B: "))
    p = int(input("Enter columns of Matrix B: "))
    print("Matrix A:")
    a = read_matrix(m, n)
    print("Matrix B:")
    b = read_matrix(n, p)
    print("A x B:")
    print_matrix(multiply_matrices(a, b))
 
else:
    print("Invalid choice")
