'''
1) product_code_generator_matrix (G matrix genetator)
2) product_code_parity_check_matrix (H matrix genetator)
3) get_set_of_matrices (Both G & H matrix for given length)
4) product_code_parity_check_matrix_advanced (H matrix genetator for tanner graph)
3) get_set_of_matrices_advanced (Both G & H matrix for given length for tanner graph)
'''
import math
def product_code_generator_matrix(n, k, rows, columns):
    G_matrix = [ [0] * k for _ in range(n - 1) ]
    for i in range(k):
        G_matrix[i][i] = 1
    for i in range(rows):
        G_matrix[i + k ][i * columns : (i + 1) * columns ] = [1] * columns    
    for i in range(columns):
        j = 0
        while(j < k):
            G_matrix[ i + k + rows][i + j] = 1
            j += rows
    G_matrix.append([1] * k)
    return G_matrix

def product_code_parity_check_matrix(n, k, rows, columns):
    support_matrix = product_code_generator_matrix(n, k, rows, columns)
    H_matrix = support_matrix[k : n]
    for temp in range(len(H_matrix)):
        H_matrix[temp].extend([0] * (n - k))
        H_matrix[temp][temp + k] = 1
    return H_matrix

def get_set_of_matrices(length):
    devisor = int(math.sqrt(length))
    while length % devisor != 0:
        devisor -= 1
    rows = devisor
    columns = int(length / devisor)
    n = (rows + 1) * (columns + 1)
    G_H_set = []
    G_matrix = product_code_generator_matrix(n, length, rows, columns)
    G_H_set.append(G_matrix)
    H_matrix = product_code_parity_check_matrix(n, length, rows, columns)
    G_H_set.append(H_matrix)
    return G_H_set

def product_code_parity_check_matrix_advanced(n, k, rows, columns):
    support_matrix = product_code_generator_matrix(n, k, rows, columns)
    H_matrix = support_matrix[k : n]
    for temp in range(len(H_matrix)):
        H_matrix[temp].extend([0] * (n - k))
        H_matrix[temp][temp + k] = 1
    H_matrix.append([0] * n)
    H_matrix.append([0] * n)
    H_matrix[n - k ][ k : k + rows ] = [1] * (rows)
    H_matrix[n - k + 1][ k + rows : k + (2 * columns) ] = [1] * (columns)
    H_matrix[n - k + 1][ n - 1 ] = 1
    H_matrix[n - k][ n - 1 ] = 1
    return H_matrix


def get_set_of_matrices_advanced(length):
    devisor = int(math.sqrt(length))
    while length % devisor != 0:
        devisor -= 1
    rows = devisor
    columns = int(length / devisor)
    n = (rows + 1) * (columns + 1)
    G_H_set = []
    G_matrix = product_code_generator_matrix(n, length, rows, columns)
    G_H_set.append(G_matrix)
    H_matrix = product_code_parity_check_matrix_advanced(n, length, rows, columns)
    G_H_set.append(H_matrix)
    return G_H_set
#print(product_code_parity_check_matrix(9, 4, 2, 2))


def product_code_parity_check_matrix2(n, k, rows, columns):
    support_matrix = product_code_generator_matrix(n, k, rows, columns)
    H_matrix = support_matrix[k : n]
    for temp in range(len(H_matrix)):
        H_matrix[temp].extend([0] * (n - k))
        H_matrix[temp][temp + k] = 1
    H_matrix[n - k - 1][0 : k] = [0] * k
    H_matrix[n - k - 1][k : k + rows ] = [1] * (rows)
    return H_matrix

def get_set_of_matrices2(length):
    devisor = int(math.sqrt(length))
    while length % devisor != 0:
        devisor -= 1
    rows = devisor
    columns = int(length / devisor)
    n = (rows + 1) * (columns + 1)
    G_H_set = []
    G_matrix = product_code_generator_matrix(n, length, rows, columns)
    G_H_set.append(G_matrix)
    H_matrix = product_code_parity_check_matrix2(n, length, rows, columns)
    G_H_set.append(H_matrix)
    return G_H_set

'''
Test:
k = 4
G_H_set1 = get_set_of_matrices(k)
G_H_set2 = get_set_of_matrices2(k)
G_H_set3 = get_set_of_matrices_advanced(k)
print("\nGenerator matrix:")
for temp in G_H_set1[0]:
    print(temp)
print("\nH matrix1:")
for temp in G_H_set1[1]:
    print(temp)
print("\nH matrix2:")
for temp in G_H_set2[1]:
    print(temp)
print("\nH matrix advanced:")
for temp in G_H_set3[1]:
    print(temp)
'''