a = [[1, 2, 3], [4, 5, 6]]
print("Original Matrix:")
for row in a:
    print(row)
print("Transpose:")
for i in range(3):
    for j in range(2):
        print(a[j][i], end=" ")
    print()
