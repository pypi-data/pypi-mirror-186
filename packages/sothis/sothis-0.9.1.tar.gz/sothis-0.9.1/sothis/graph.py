"""
Name: graph.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: graph api
"""

import typing
from . import structures
from .helpers import print_list
from collections import deque
import random

DISTANCE_KEY = "distance"
PATH_KEY = "path"


class edge(object):
    def __init__(self, v, w, weight=0.0):
        self.v = v
        self.w = w
        self.weight = weight
    
    def __gt__(self, other):
        return self.weight > other
    
    def __ge__(self, other):
        return self.weight >= other
    
    def __lt__(self, other):
        return self.weight < other
    
    def __le__(self, other):
        return self.weight <= other
    
    def __str__(self):
        return "%d-%d %.5f" % (self.v, self.w, self.weight)
    
    def __repr__(self):
        return str(self)


class Graph:
    """
    undirected weighted graph structure
    """
    
    def __init__(self, fmt=None):
        self.nodes = dict()
        self.V = 0
        self.E = 0
        self.fmt = fmt if fmt else str
        self.edges = []
    
    def vertices(self) -> typing.Iterable:
        """return iterable of all the vertices in the graph"""
        return iter(list(self.nodes.keys()))
    
    def dfs(self, v, visited=None):
        """
        depth first search with a starting node v returning a
        depth first tree rooted at v
        :param v: starting node
        :return: a list of vertices on the DFS path starting from v
        """
        if visited is None:
            visited = [v]
        for e in self.nodes[v]:
            if e not in visited:
                visited.append(e)
                self.dfs(e, visited)
        return visited
    
    def bfs(self, v):
        """
        breadth first search with a starting node v returning a
        breadth first tree rooted at v
        :param v: starting node
        :return: a list of vertices on the BFS path starting from v
        """
        visited = [v]
        Q = [v]
        while Q:
            w = Q[0]
            Q = Q[1:]
            for u in self.nodes[w]:
                if u not in visited:
                    visited.append(u)
                    Q.append(u)
        return visited
    
    def add_edge(self, v: typing.Any, w: typing.Any, weight=0, directed=False) -> bool:
        """adds a new edge into the graph"""
        if v == w:
            raise ValueError("source and destination are the same")
        # add vertices to graph if they don't already exist
        if v not in self.nodes:
            self.nodes[v] = {}
            self.V += 1
        if w not in self.nodes:
            self.nodes[w] = {}
            self.V += 1
        # check that the edges do not already exist
        if (not directed) and (v in self.nodes[w]):
            return
        if w in self.nodes[v]:
            return
        # add edge
        self.nodes[v][w] = weight
        if not directed:
            self.nodes[w][v] = weight
        self.E += 1
        e = edge(v, w, weight)
        self.edges.append(e)
    
    def adjacent(self, v):
        """
        return list of all adjacent nodes to a given node v
        :param v: graph node
        :return: list of incident edges to v
        """
        if v not in self.nodes: raise ValueError
        return self.nodes[v]
    
    def weight(self, v, w):
        if v not in self.nodes or w not in self.nodes: raise ValueError
        return self.nodes[v][w]
    
    def path(self, src, dest) -> typing.Iterable:
        """
        returns a iterable of the shortest path from a given source to
        a destination node in the graph if such a path exists
        :param src: starting vertex
        :param dest: ending vertex
        :return: a list iterable of the path from source to destination
        or an empty iterable if no path between the vertices exists
        """
        if not self.haspath(src, dest):
            return iter([])
        if dest not in self.vertices():
            return iter([])
        path = deque()
        # get the shortest paths data of the source vertex
        (length, prev) = self.__djikstra(src)
        e = prev[dest]
        path.appendleft(dest)
        # trace backward along path and push into path stack
        while e != None:
            path.appendleft(e)
            e = prev[e]
        return iter(list(path))
    
    def haspath(self, src, dest) -> bool:
        """
        returns whether there is a path in the graph from
        a given source vertex to a given destination vertex
        :param src: starting vertex
        :param dest: target vertex
        :return: True or False
        """
        if src not in self.vertices() or dest not in self.vertices():
            return IndexError(f"One or more of the arguments do not exist in graph")
        (length, prev) = self.__djikstra(src)
        return length[dest] < float('+inf')
    
    def __djikstra(self, s):
        """
        utility function
        using djikstra's algorithm return two
        dictionarys of the shortest path from a given
        starting node to each other vertex in the graph
        and a dictionary of each node and its previous node
        along a path
        :param s: starting vertex
        :return: a tuple of dictionaries
        """
        length = {}
        prev = {}
        for v in self.vertices():
            length[v] = float('+inf')
            prev[v] = None
        length[s] = 0.0
        
        # initialize priority queue where all nodes are organized
        # by their distance to the starting node
        pq = structures.priority_queue(key=lambda x: length[x], maxsize=self.V)
        pq.put(s)
        while pq:
            v = pq.min()
            for w in self.adjacent(v):
                d = length[v] + self.nodes[v][w]
                if d < length[w]:  # update to minimum path length
                    length[w] = d
                    prev[w] = v
                    # priority queue value updates
                    if w not in pq:
                        pq.put(w)
                    else:
                        pq.update(w, w)
        
        return (length, prev)
    
    def degree(self, v):
        """ return number of edges v is involved in """
        if v not in self.nodes: raise ValueError
        return len(self.nodes[v])
    
    def max_degree(self):
        """returns the largest degree out of all vertices"""
        m = 0
        for v in self.nodes:
            d = self.degree(v)
            m = d if d > m else m
        return m
    
    def average_degree(self):
        """return average degree"""
        return (2 * self.E) / self.V
    
    def __str__(self) -> str:
        out = f"Vertices: {self.V}\nEdges: {self.E}\n"
        for i, v in enumerate(self.nodes):
            out += (self.fmt(v) + '\n')
            for w in self.nodes[v]:
                out += "\t{} -> {}: {}".format(self.fmt(v), self.fmt(w), self.nodes[v][w]) + '\n'
        return out[:-1]
