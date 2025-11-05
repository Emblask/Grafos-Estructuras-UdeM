from typing import Any
import math

class GraphMatrix:
    def __init__(self):
        self.adj_matrix: list[list[float]] = []
        self.nodes: list[Any] = []
        self.size: int = 0
        self.precio_diesel = 5000
        self.km_por_galon = 10

    # Agregar un nodo
    def add_vertex(self, value: Any) -> None:
        if value in self.nodes:
            return None
        self.nodes.append(value)
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * (self.size + 1))
        self.size += 1

    # Agregar relaciones entre nodos
    def add_edge(self, vertex_1: Any, vertex_2: Any, distance: float, directed: bool = False):
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)
        i, j = self.nodes.index(vertex_1), self.nodes.index(vertex_2)
        self.adj_matrix[i][j] = distance
        if not directed:
            self.adj_matrix[j][i] = distance

    # Mostrar matriz
    def show_matrix(self):
        print("Matriz de adyacencia (km):")

        print("   |", end="")
        for node in self.nodes:
            print(f"{node:^3}|", end="")
        print()
        print("-" * (5*len(self.nodes)))

        for i in range(len(self.nodes)):
            print(f"{self.nodes[i]:^3}|", end="")
            for j in range(len(self.nodes)):
                print(f"{self.adj_matrix[i][j]:^3}|", end="")
            print()

    # Calcular costo
    def calculate_cost(self, distancia_total: int) -> float:
        galones = distancia_total / self.km_por_galon
        return galones * self.precio_diesel

    # Árbol de expansión mínima (Prim)
    def minimum_spanning_tree(self):
        if self.size == 0:
            print("El grafo está vacío")
            return

        selected = [True] + [False] * (self.size - 1)
        edges_mst = []
        total_distance = 0

        while len(edges_mst) < self.size - 1:
            min_edge = math.inf
            x = y = -1

            for i in range(self.size):
                if selected[i]:
                    for j in range(self.size):
                        distance = self.adj_matrix[i][j]
                        if not selected[j] and 0 < distance < min_edge:
                            min_edge, x, y = distance, i, j

            edges_mst.append((self.nodes[x], self.nodes[y], min_edge))
            total_distance += min_edge
            selected[y] = True

        costo_total = self.calculate_cost(total_distance)

        def mostrar_resultados():
            print("\nAristas seleccionadas:")
            for i, j, k in edges_mst:
                print(f"{i} — {j} : {k} km")

            print(f"\nDistancia total mínima: {total_distance} km")
            print(f"Costo total estimado: {costo_total} pesos")

            dicc = {n: [] for n in self.nodes}
            for i, j, k in edges_mst:
                dicc[i].append((j, k))
                dicc[j].append((i, k))

            class TreeNode:
                def __init__(self, value):
                    self.value = value
                    self.children: list[tuple['TreeNode', float]] = []

            def build_tree(root_value, visited=None):
                if visited is None:
                    visited = []
                visited.append(root_value)
                node = TreeNode(root_value)
                for neighbor, distance in dicc[root_value]:
                    if neighbor not in visited:
                        child = build_tree(neighbor, visited)
                        node.children.append((child, distance))
                return node

            tree = build_tree(self.nodes[0], [])

            def print_tree(node: TreeNode, prefix: str = "", is_last: bool = True):
                connector = "└── " if is_last else "├── "
                print(prefix + connector + str(node.value))

                child_count = len(node.children)
                for idx, (child_node, distance) in enumerate(node.children):
                    is_child_last = (idx == child_count - 1)
                    next_prefix = prefix + ("    " if is_last else "│   ")
                    print(next_prefix + ("└── " if is_child_last else "├── ") + f"({distance} km)")
                    print_tree(child_node, next_prefix + ("    " if is_child_last else "│   "), True)

            print("\nRepresentación del árbol:")
            print(tree.value)
            for idx, (child_node, distance) in enumerate(tree.children):
                is_child_last = (idx == len(tree.children) - 1)
                print(("└── " if is_child_last else "├── ") + f"({distance} km)")
                print_tree(child_node, ("    " if is_child_last else "│   "), True)

        mostrar_resultados()

    # Backtracking
    def optimal_route(self, start: Any):
        if start not in self.nodes:
            print("Nodo inicial no existe en el grafo.")
            return
        start_idx = self.nodes.index(start)
        visited = [False] * self.size
        best_path = []
        best_distance = math.inf

        def backtrack(current_idx, count, dist_total, path):
            nonlocal best_distance, best_path
            if count == self.size and self.adj_matrix[current_idx][start_idx] > 0:
                dist_total += self.adj_matrix[current_idx][start_idx]
                if dist_total < best_distance:
                    best_distance = dist_total
                    best_path = path + [start]
                return

            for next_idx in range(self.size):
                if not visited[next_idx] and self.adj_matrix[current_idx][next_idx] > 0:
                    visited[next_idx] = True
                    backtrack(next_idx, count + 1, dist_total + self.adj_matrix[current_idx][next_idx], path + [self.nodes[next_idx]])
                    visited[next_idx] = False

        visited[start_idx] = True
        backtrack(start_idx, 1, 0, [start])

        costo_total = self.calculate_cost(best_distance)
        print(f"\nRuta más eficiente: {' -> '.join(best_path)}")
        print(f"Distancia mínima: {best_distance} km")
        print(f"Costo total estimado: {costo_total} pesos")




# EJM
grafo = GraphMatrix()
grafo.add_edge("A", "B", 10)
grafo.add_edge("A", "C", 15)
grafo.add_edge("A", "D", 20)
grafo.add_edge("A", "E", 25)
grafo.add_edge("B", "C", 35)
grafo.add_edge("B", "D", 25)
grafo.add_edge("B", "E", 30)
grafo.add_edge("C", "D", 30)
grafo.add_edge("C", "E", 20)
grafo.add_edge("D", "E", 15)

grafo.show_matrix()
grafo.minimum_spanning_tree()
grafo.optimal_route("A")
