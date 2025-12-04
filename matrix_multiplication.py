rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("enter elements: ")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print("matrix: ")
for j in matrix:
    print(j)
a=[1,2,3]
b=[4,5,6]

#dot product:
a = [1, 2, 3]
b = [4, 5, 6]

dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]

print("Dot Product =", dot)

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
C = [[0, 0],
     [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j]+=A[i][k]*B[k][j]
for l in C:
    print(l)