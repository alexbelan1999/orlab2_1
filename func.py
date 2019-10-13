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

def Dijkstra(nodes, edges_with_weight, start, end):
    vertex = len(nodes)
    bool_arr = [False] * 10
    int_arr = [0] * 10
    adj_matrix = Adjacency_matrix(nodes, edges_with_weight)

    d = [math.inf] * 10
    d[start] = 0

    for i in range(1, vertex + 1):
        v = -1
        for j in range(1, vertex + 1):
            if (not bool_arr[j] and (v == -1 or d[j] < d[v])):
                v = j
        if (d[v] == math.inf):
            break

        bool_arr[v] = True

        print('Рассматривается вершина: ',v)

        for j in range(1, vertex + 1):
            edge_weight = adj_matrix[v][j]
            if (edge_weight < math.inf and (d[v] + edge_weight < d[j])):
                d[j] = d[v] + edge_weight
                int_arr[j] = v
            print('l`(', j ,') = ', d[j])

        if (v == end):
            break

    result = []
    if (d[end] == math.inf):
        return result

    ind = 0

    i = end
    while (i != start):
        res = []
        res.append(int_arr[i])
        res.append(i)
        res.append(adj_matrix[int_arr[i]][i])
        result.append(res)
        i = int_arr[i]
        ind += 1

    result.reverse()

    return result
