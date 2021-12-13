class Graph:
    def __init__(self):
        self.nodes = {}
    
    def find_paths(self, current_path=['start'], end='end'):
        current = current_path[-1]
        for node in self.nodes[current]:
            new_path = current_path + [node]
            if node == end:
                yield new_path
            elif node.isupper() or node not in current_path:
                yield from self.find_paths(new_path, end) 


    def add_edge(self, start, end):
        if not start in self.nodes:
            self.nodes[start] = set()
        self.nodes[start].add(end)
        if not end in self.nodes:
            self.nodes[end] = set()
        self.nodes[end].add(start)

if __name__ == '__main__':
    g = Graph()
    with open('input.txt', 'r') as f:
        for start, end in [line.split('-') for line in f.read().splitlines()]:
            g.add_edge(start, end)
    
    print(sum([1 for _ in g.find_paths()]))