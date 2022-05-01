import numpy as np

import operations as op


matrix_a = np.array([[1,2,2]
             ,[4,4,2]
             ,[4,6,4]],float)

# In: matrix_a -> Any matrix
# Out: The scalar of the matrix matrix_a 
def gauss_elimination(matrix_a):
    """Função que recebe uma matriz e retorna ela escalonada"""

    for i in range(0, len(matrix_a)): 
        for j in range(i+1, len(matrix_a)):
            for k in range(i, len(matrix_a)): 
                print((matrix_a[j][i] / matrix_a[i][i]), j,k)

                matrix_a[j][k] = matrix_a[j][k] - (matrix_a[j][i] / matrix_a[i][i]) * matrix_a[i][k]
                
    return matrix_a


# print(gauss_elimination(matrix_a))
def solve_equation(N = 0, ICOD = 1, IDET = 0, A = 0, B = 0, TolM = 0.01):

    if (ICOD == 1): # Decomposição LU   
        # Transformação de matrix_a em LU
        for i in range(0, len(matrix_a)):
            for j in range(i+1, len(matrix_a)):
                if matrix_a[i][i] == 0:
                    matrix_a = op.pivot(matrix_a, i)

                matrix_a[j][i] = matrix_a[j][i] / matrix_a[i][i]
            for k in range(i+1, len(matrix_a)):
                for l in range(i+1, len(matrix_a)):
                    matrix_a[l][k] = matrix_a[l][k] - matrix_a[l][i] * matrix_a[i][k]
        
        return matrix_a

    elif (ICOD == 2): # Cholesky decomposition
        pass
    elif (ICOD == 3): # Jacobi Method
        pass
    elif (ICOD == 4): # Gauss-Seidel Method
        pass

    else:
        print("Invalid ICOD")
    return 0

print("\n --- \n")
print(solve_equation(A=matrix_a))