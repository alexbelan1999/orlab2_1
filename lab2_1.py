import matplotlib.pyplot as plt
import networkx as nx

import func

# nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nodes = [1, 2, 3, 4]
var = 0
start = 0
end = 0
while var not in [1, 2]:
    var = int(input("Введите 1 для метода Дейкстры или 2 для метода Флойда: "))

while start not in nodes:
    start = int(input("Введите начальную вершину: "))

while end not in nodes:
    end = int(input("Введите конечную вершину: "))
edges_with_weight = [(1, 2, 1), (1, 3, 6), (2, 3, 4), (2, 4, 1), (4, 3, 1)]
# edges_with_weight = [(1,2,10), (1,4,5), (2,3,3), (2,5,9) , (3,6,11), (4,2,5), (4,5,10), (4,7,6), (4,8,15), (5, 6,13), (5,8,10), (5,9,5), (6,9,7), (7,8,8), (8,9,4)]
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges_with_weight)

layout = nx.spring_layout(G)
nx.draw(G, layout, with_labels=True, node_color='b')
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
plt.show()

if var == 1:
    algoritm_d = func.Dijkstra(nodes, edges_with_weight, start, end)
    if len(algoritm_d) == 0:
        print("Нет пути из вершины ", start, " в вершину ", end)
    else:
        sum_d = 0
        for i in range(0, len(algoritm_d)):
            sum_d += algoritm_d[i][2]

        algoritm_d = func.TMatrix(algoritm_d)
        nodes1 = algoritm_d[0]
        str_path_d = ' --> '.join(str(x) for x in algoritm_d[0])

        print("Алгоритм Дейкстры: ")
        print("Путь: ", str_path_d, "-->", end, ", длина пути = ", sum_d)

        nodes1.append(end)
        dedge = []
        for d in edges_with_weight:
            if d[0] in nodes1 and d[1] in nodes1:
                dedge.append(d)

        G1 = nx.DiGraph()
        G1.add_nodes_from(nodes1)
        G1.add_weighted_edges_from(dedge)

        layout1 = nx.spring_layout(G1)
        nx.draw(G1, layout1, with_labels=True, node_color='b')
        labels1 = nx.get_edge_attributes(G1, "weight")
        nx.draw_networkx_edge_labels(G1, pos=layout1, edge_labels=labels1)
        plt.show()

elif var == 2:
    algoritm_f = func.Floyd(nodes, edges_with_weight, start, end)
    if len(algoritm_f) == 0:
        print("Нет пути из вершины ", start, " в вершину ", end)
    else:
        sum_d = 0
        for i in range(0, len(algoritm_f)):
            sum_d += algoritm_f[i][2]

        algoritm_f = func.TMatrix(algoritm_f)
        nodes1 = algoritm_f[0]
        str_path_f = ' --> '.join(str(x) for x in algoritm_f[0])

        print("Алгоритм Флойда: ")
        print("Путь: ", str_path_f, "-->", end, ", длина пути = ", sum_d)
        nodes1.append(end)
        dedge = []
        for d in edges_with_weight:
            if d[0] in nodes1 and d[1] in nodes1:
                dedge.append(d)

        G1 = nx.DiGraph()
        G1.add_nodes_from(nodes1)
        G1.add_weighted_edges_from(dedge)

        layout1 = nx.spring_layout(G1)
        nx.draw(G1, layout1, with_labels=True, node_color='b')
        labels1 = nx.get_edge_attributes(G1, "weight")
        nx.draw_networkx_edge_labels(G1, pos=layout1, edge_labels=labels1)
        plt.show()
else:
    print("Неправильно выбран алгоритм!")
