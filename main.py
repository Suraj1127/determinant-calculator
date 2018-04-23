import numpy as np


def calculate_determinant(matrix):
    """
    Takes in matrix and gives determinant.
    """
    # Base case for matrix of shape (2,2)
    if matrix.shape[0] == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    # Implement recursion function.
    determinant = 0
    for i in range(matrix.shape[0]):
        temp_matrix = matrix[1:,:].copy()
        temp_matrix = np.delete(temp_matrix, i, 1)
        determinant = determinant + ((-1)**i)*matrix[0][i]*calculate_determinant(temp_matrix)
    return determinant


def main():
    # Get the shape of the matrix.
    n = int(input("Enter the no of columns of the square matrix:\n").strip())

    # Get the square matrix from user.
    matrix = np.zeros((n,n))
    print("\nEnter the matrix in the format such that each row is in\n"
          "different line and each element in a row is separated by\n"
          "a space.\n")
    for i in range(n):
        matrix[i] = [int(j) for j in input().split()]

    print("So, the determinant is", calculate_determinant(matrix))


if __name__ == "__main__":
    main()