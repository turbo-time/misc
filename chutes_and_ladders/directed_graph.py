class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, label, input_node, output_node):
        self.nodes[label] = {'input': input_node, 'output': output_node}

    def load_from_file(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                label, input_node, output_node = line.strip().split(',')
                input_node = None if input_node == 'X' else int(input_node)
                output_node = None if output_node == 'X' else int(output_node)
                self.add_node(int(label), input_node, output_node)

    def __str__(self):
        result = []
        for label, connections in self.nodes.items():
            result.append(f"Node {label}: input -> {connections['input']}, output -> {connections['output']}")
        return "\n".join(result)

# Example usage:
graph = DirectedGraph()
graph.load_from_file('/home/nick/source/misc/graph.txt')
print(graph)
