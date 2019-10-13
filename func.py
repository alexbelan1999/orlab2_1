def TMatrix(A):
    m = len(A)
    n = len(A[0])
    AT = [[0] * m for i in range(n)]
    for i in range(0,n):
        for j in range(0,m):
            AT[i][j] = A[j][i]
    return AT