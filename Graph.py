import networkx as nx


class Graph:
    def __init__(self, directed=False):
        self.graph = nx.DiGraph() if directed else nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, a, b, weight=None):
        self.graph.add_edge(a, b, weight=weight)

    def remove_node(self, node):
        self.graph.remove_node(node)

    def remove_edge(self, a, b):
        self.graph.remove_edge(a, b)

    def analyze(self):
        g = self.graph
        loops = list(nx.nodes_with_selfloops(g))

        print("Uzly:", g.number_of_nodes())
        print("Hrany:", g.number_of_edges())
        print("Orientovaný:", g.is_directed())
        print("Ohodnocený:", any(
            "weight" in data for _, _, data in g.edges(data=True)
        ))
        print("Smyčky:", loops)
        print("Souvislý:", nx.is_weakly_connected(g)
              if g.is_directed() else nx.is_connected(g))
        print("Planární:", nx.check_planarity(nx.Graph(g))[0])

        if loops:
            print("Chromatické číslo: nedefinováno kvůli smyčce")
        else:
            print("Chromatické číslo:",
                  max(nx.coloring.greedy_color(nx.Graph(g)).values(),
                      default=-1) + 1)


graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C", 5)
graph.add_edge("C", "A", 10)
graph.add_node("D")

graph.analyze()
