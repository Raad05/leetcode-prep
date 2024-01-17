# Uses Queue
graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}

def bfs(graph, node):
    visited = [node]
    queue = [node]

    while queue:
        current = queue.pop(0)
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited

print(bfs(graph, "5"))