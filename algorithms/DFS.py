# Can be done using stack(faster) or recursion(slower)
graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}

def dfs(graph, node):
    visited = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(graph[current][::-1])
    return visited


print(dfs(graph, "5"))