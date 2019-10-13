import math
def TMatrix(A):
    m = len(A)
    n = len(A[0])
    AT = [[0] * m for i in range(n)]
    for i in range(0,n):
        for j in range(0,m):
            AT[i][j] = A[j][i]
    return AT

def Adjacency_matrix(nodes,edges_with_weight):
    vertex = len(nodes)
    adj_matrix = [[None] * (vertex + 1) for i in range(vertex + 1)]

    for i in range(1, vertex + 1):
        for j in range(1, vertex + 1):
            if (i == j):
                adj_matrix[i][j] = 0
            else :
                adj_matrix[i][j] = math.inf

    for k in range(0,len(edges_with_weight)):
        adj_matrix[edges_with_weight[k][0]][edges_with_weight[k][1]] = edges_with_weight[k][2]

    return adj_matrix
