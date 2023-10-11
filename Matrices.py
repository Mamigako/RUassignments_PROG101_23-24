"""Output addition of 2 matrices"""

Matrix_1_1 = []
Matrix_1_2 = []
Matrix_2_1 = []
Matrix_2_2 = []
Matrix_3_1 = []
Matrix_3_2 = []

List_of_matrix_a = []
List_of_matrix_b = []
List_of_matrix_c = []


for i in range(3):
    values = int(input())
    Matrix_1_1.append(values)

for i in range(3):
    values = int(input())
    Matrix_1_2.append(values)

for i in range(3):
    values = int(input())
    Matrix_2_1.append(values)

for i in range(3):
    values = int(input())
    Matrix_2_2.append(values)


c1 = int(Matrix_1_1[0]) + int(Matrix_2_1[0])
Matrix_3_1.append(c1)

c2 = int(Matrix_1_1[1]) + int(Matrix_2_1[1])
Matrix_3_1.append(c2)

c3 = int(Matrix_1_1[2]) + int(Matrix_2_1[2])
Matrix_3_1.append(c3)

c4 = int(Matrix_1_2[0]) + int(Matrix_2_2[0])
Matrix_3_2.append(c4)

c5 = int(Matrix_1_2[1]) + int(Matrix_2_2[1])
Matrix_3_2.append(c5)

c6 = int(Matrix_1_2[2]) + int(Matrix_2_2[2])
Matrix_3_2.append(c6)

List_of_matrix_a.append(Matrix_1_1)
List_of_matrix_a.append(Matrix_1_2)
List_of_matrix_b.append(Matrix_2_1)
List_of_matrix_b.append(Matrix_2_2)
List_of_matrix_c.append(Matrix_3_1)
List_of_matrix_c.append(Matrix_3_2)

print(List_of_matrix_a)
print(List_of_matrix_b)
print(List_of_matrix_c)