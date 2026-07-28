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

def read_matrix(rows, cols, label=""):
    """Read a matrix of given dimensions from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1}{' of ' + label if label else ''}: ")
            values = raw.split()
            if len(values) != cols:
                print(f"Error: expected {cols} values, got {len(values)}. Try again.")
                continue
            matrix.append([int(v) for v in values])
            break
    return matrix


def print_matrix(matrix, title=""):
    """Display a matrix in a neat, aligned grid."""
    if title:
        print(title)

    # Find the widest number so every column lines up
    width = 0
    for row in matrix:
        for val in row:
            width = max(width, len(str(val)))

    for row in matrix:
        line = "  ".join(str(val).rjust(width) for val in row)
        print(line)
    print()


def transpose_matrix(matrix):
    """Return the transpose of an M x N matrix (result is N x M)."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B. A is M x N, B is N x P, result is M x P."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print_matrix(matrix, "\nOriginal Matrix:")
    result = transpose_matrix(matrix)
    print_matrix(result, "Transposed Matrix:")


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    print_matrix(matrix_a, "\nMatrix A:")
    print_matrix(matrix_b, "Matrix B:")

    result = add_matrices(matrix_a, matrix_b)
    print_matrix(result, "Sum (A + B):")


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    matrix_a = read_matrix(m, n, "Matrix A")
    matrix_b = read_matrix(n, p, "Matrix B")

    print_matrix(matrix_a, "\nMatrix A:")
    print_matrix(matrix_b, "Matrix B:")

    result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(result, "Product (A x B):")


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = input("Choose an operation (1-3): ")

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Error: Invalid choice.")

main()