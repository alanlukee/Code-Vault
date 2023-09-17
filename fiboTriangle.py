def generate_fibonacci_triangle(rows):
    triangle = []
    a, b = 0, 1
    for i in range(1,rows+1,1):
        row = []
        for j in range(1,i+1,1):
            row.append(a)
            a, b = b, a + b
        triangle.append(row)
    return triangle

num_rows = int(input("Enter the number of rows for the Fibonacci triangle: "))

fibonacci_triangle = generate_fibonacci_triangle(num_rows)

# Printing the Fibonacci triangle
for row in fibonacci_triangle:
    print(" ".join(map(str, row)))