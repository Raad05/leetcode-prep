class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for i in new_paths:
                    paths.append(i)

        return paths
    
    def get_shortest_path(self, start, end, path = []):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

routes = [
    ("Dhaka", "Bogura"),
    ("Tangail", "Bogura"), 
    ("Dhaka", "Barishal"), 
    ("Bogura", "Barishal")
]

graph_route = Graph(routes)

start = "Dhaka"
end = "Barishal"
print(graph_route.get_paths(start, end))
print(graph_route.get_shortest_path(start, end))