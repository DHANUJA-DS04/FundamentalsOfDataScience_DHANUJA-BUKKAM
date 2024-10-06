import numpy as np

def generate_matrix(seed, shape, low, high):
    np.random.seed(seed)
    return np.random.randint(low, high, size=shape)

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def replace_matrix_values(matrix):
    new_matrix = np.zeros_like(matrix)
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[2]):
                value = matrix[i, j, k]
                
                condition_0 = (i % 2 != 0)  # Index 0 is odd
                condition_1 = is_prime(k)  # Index 1 is prime
                condition_2 = (j % 2 == 0)  # Index 2 is even
                
                if condition_0 and condition_1 and condition_2:
                    new_matrix[i, j, k] = 1
                else:
                    new_matrix[i, j, k] = 0

    return new_matrix

def find_longest_segment(matrix):
    longest_length = 0
    longest_coords = None
    direction = None
    
    # Check horizontal segments
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            length = 0
            start_col = 0
            for k in range(matrix.shape[2]):
                if matrix[i, j, k] == 1:
                    if length == 0:
                        start_col = k
                    length += 1
                else:
                    if length > longest_length:
                        longest_length = length
                        longest_coords = (i, j, start_col)
                        direction = "horizontal"
                    length = 0
            if length > longest_length:
                longest_length = length
                longest_coords = (i, j, start_col)
                direction = "horizontal"
    
    # Check vertical segments
    for i in range(matrix.shape[0]):
        for k in range(matrix.shape[2]):
            length = 0
            start_row = 0
            for j in range(matrix.shape[1]):
                if matrix[i, j, k] == 1:
                    if length == 0:
                        start_row = j
                    length += 1
                else:
                    if length > longest_length:
                        longest_length = length
                        longest_coords = (i, start_row, k)
                        direction = "vertical"
                    length = 0
            if length > longest_length:
                longest_length = length
                longest_coords = (i, start_row, k)
                direction = "vertical"
    
    return longest_length, longest_coords, direction

def main():
    # Define parameters
    seed = 49
    shape = (7, 7, 7)
    low = 0
    high = 20

    # Generate the matrix
    matrix = generate_matrix(seed, shape, low, high)
    print("Original matrix:")
    print(matrix)

    # Replace values in the matrix
    new_matrix = replace_matrix_values(matrix)
    print("\nModified matrix:")
    print(new_matrix)

    # Find the longest segment
    longest_length, longest_coords, direction = find_longest_segment(new_matrix)

    print(f"\nLongest segment length: {longest_length}")
    print(f"Coordinates of the start of the longest segment: {longest_coords}")
    print(f"Direction of the longest segment: {direction}")

if __name__ == "__main__":
    main()
