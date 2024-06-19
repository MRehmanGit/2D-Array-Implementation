r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
# Create a 2D array (matrix) with 'r' rows and 'c' columns
# Each element in the row is initialized to its column index
matrix = [[i for i in range (c)] for j in range(r)]
# Print the resulting matrix
print(matrix)
