#!/usr/bin/env python3.2
# dfs.py
# By Simon David Pratt
# Copyright 2013

# I chose this code as sample code for my application to Dartmouth
# because it is a complete program including test code in less than
# 100 lines that elegantly implements one of Computer Science's most
# useful algorithms: Depth-First Search (DFS).

class DirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.adj = {}
        
    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.adj[v] = []

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        self.adj[u].append(v)

    @staticmethod
    def edgeInList(edge, l):
        return edge in l

    # Depth-First Search
    # Input: The only public parameter is start, which is the node at
    # which to start the DFS traversal
    # Output: Note that nodes with the same low number form a cycle
    def dfs(self, start, _parent=None, _tree_edges=None,
            _back_edges=None, _pre=None, _low=None, _count=0):
        if start not in self.adj:
            return None, None, None, None, None
        if _parent == None:
            _tree_edges = []
            _back_edges = []
            _pre = {}
            _low = {}
        _pre[start] = _count
        _low[start] = _count
        for v in self.adj[start]:
            if v not in _pre: # not visited before
                _tree_edges.append((start,v))
                _tree_edges, _back_edges, _pre, _low, _count = self.dfs(v,
                                                                   start,
                                                                   _tree_edges,
                                                                   _back_edges,
                                                                   _pre,
                                                                   _low,
                                                                   _count+1)
                _low[start] = min(_low[start],_low[v])
            else:
                if not (self.edgeInList((start,v), _tree_edges) or
                        self.edgeInList((start,v), _back_edges)):
                    _back_edges.append((start,v))
                if v != _parent:
                    _low[start] = min(_low[start],_pre[v])
        return _tree_edges, _back_edges, _pre, _low, _count

class Graph(DirectedGraph):
    def addEdge(self, u, v):
        super().addEdge(u, v)
        super().addEdge(v, u)

    @staticmethod
    def edgeInList(edge, l):
        return (edge in l) or ((edge[1],edge[0]) in l)

def printResults(t, b, p, l, _):
    print("Tree edges: {}".format(t))
    print("Back edges: {}".format(b))
    print("Prenumbers: {}".format(p))
    print("Lownumbers: {}".format(l))
        
def main():
    graph = Graph()
    print("DFS('a') on empty graph ======================================")
    printResults(*graph.dfs('a'))
    graph.addEdge('a','b')
    graph.addEdge('b','c')
    graph.addEdge('c','d')
    graph.addEdge('d','b')
    print("DFS('a') on small graph ======================================")
    printResults(*graph.dfs('a'))
    for d in range(2,6):
        print("DFS(2) on K{} ================================================="
              .format(d))
        g = Graph()
        for i in range(1,d+1):
            for j in range(i+1,d+1):
                g.addEdge(i,j)
        printResults(*g.dfs(2))

if __name__ == '__main__':
    main()
