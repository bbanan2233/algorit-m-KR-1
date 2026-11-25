from collections import deque


def dfs(graph, start):
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def connected_components(graph):
    visited = set()
    components = []

    for start in graph:
        if start in visited:
            continue
        component = set()
        stack = [start]
        visited.add(start)
        while stack:
            vertex = stack.pop()
            component.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        components.append(component)

    return components


def bipartite_coloring(graph, component):
    color = {}

    for start in component:
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return None

    return color


def topological_sort(graph):
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)
        order.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            visit(vertex)

    return order[::-1]


def shortest_path_bfs(graph, start, target):
    parent = {start: None}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex == target:
            break
        for neighbor in graph[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)

    if target not in parent:
        return None

    path = []
    vertex = target
    while vertex is not None:
        path.append(vertex)
        vertex = parent[vertex]

    return path[::-1]


def main():
    graph1 = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6, 7],
        4: [2, 8],
        5: [2, 8],
        6: [3, 9],
        7: [3, 9],
        8: [4, 5, 10],
        9: [6, 7, 10],
        10: [8, 9],
    }
    print("Задание 1")
    print("DFS от 1:", dfs(graph1, 1))
    print("BFS от 1:", bfs(graph1, 1))

    graph2 = {
        "A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B", "D"],
        "D": ["C"], "E": ["F"], "F": ["E", "G"], "G": ["F"],
        "H": [], "I": ["J", "L"], "J": ["I", "K"],
        "K": ["J", "L"], "L": ["I", "K"],
    }
    print("\nЗадание 2")
    for number, component in enumerate(connected_components(graph2), 1):
        coloring = bipartite_coloring(graph2, component)
        print(f"Компонента {number}: {sorted(component)}")
        if coloring is None:
            print("  Двудольность: нет")
        else:
            parts = [sorted(v for v in component if coloring[v] == c) for c in (0, 1)]
            print(f"  Двудольность: да; доли {parts[0]} и {parts[1]}")

    graph3 = {
        "A": ["B", "C"], "B": ["D", "E"], "C": ["E", "F"],
        "D": ["G"], "E": ["G", "H"], "F": ["G"],
        "G": ["H"], "H": [],
    }
    print("\nЗадание 3")
    print("Топологический порядок:", topological_sort(graph3))
    path = shortest_path_bfs(graph3, "A", "H")
    print("Кратчайший путь A→H:", " → ".join(path))
    print("Длина пути:", len(path) - 1)


if __name__ == "__main__":
    main()
