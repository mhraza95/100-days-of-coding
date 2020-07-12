"""
Day 21 of 100 days coding 

problem 01: A Python program to demonstrate the adjacency list representation of the graph 
"""

class AdjNode:

    def __init__(self, data):

        self.vertex = data
        self.next = None


class Graph:

    def __init__(self, vertices):

        self.v = vertices
        self.graph = [None] * self.v

    def add_edge(self, src, dest):

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    def print_graph(self):

        for i in range(self.v):

            print("Adjacency list of vertex {}\n head ".format(i), end="")
            temp = self.graph[i]
            
            while temp:
                
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next

            print("\n")


V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(2, 0)
graph.add_edge(2, 1)

graph.print_graph()