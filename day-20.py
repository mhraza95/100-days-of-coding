"""
Day 20 of 100 days coding 

problem 01: Breadth First Search or BFS for a Graph
"""

from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph = defaultdict(list)


    def addGraph(self, u, v):

        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (len(self.graph))

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:

                if visited[i] == False:

                    queue.append(i)
                    visited[i] = True

            
g = Graph()
g.addGraph(0, 1)
g.addGraph(0, 2)
g.addGraph(1, 2)
g.addGraph(2, 0)
g.addGraph(2, 3)
g.addGraph(3, 3)

g.BFS(2)
