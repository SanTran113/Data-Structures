from typing import Any, List, Optional
from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key: Any, color: None, visited: False):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = color
        self.visited = visited


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''

        adjList = []
        adjDic = {}

        self.vertices = adjList
        self.vertexDic = adjDic

        with open(filename, 'r') as file:
            data = file.read()
        data = data.split('\n')
        for v in data:
            if v == '':
                break
            a = v.split(' ')
            adjList.append(a[0])
            adjList.append(a[1])

        for i in range(len(adjList)):
            if adjList[i] not in adjDic:
                self.add_vertex(adjList[i])

        self.get_vertices()

        # adjacency list
        for i in range(0, len(adjList), 2):
            # print(i)
            # print(adjList)
            self.add_edge(adjList[i], adjList[i + 1])
            # self.get_vertex(adjList[i]).adjacent_to.append(adjDic[adjList[i + 1]])
            # self.get_vertex(adjList[i + 1]).adjacent_to.append(adjDic[adjList[i]])
        # print(adjDic)

        # print(adjList)
        # Tests
        # print(self.get_vertex('v8').adjacent_to)
        # print(self.get_vertex('v1').adjacent_to)

        print(self.get_vertex('v10'))
        print(self.get_vertices())

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.vertexDic.keys():
            v = Vertex(key, None, False)
            self.vertexDic[key] = v

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.vertexDic.keys():
            return self.vertexDic[key]
        else:
            return None


    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        # Add in vertex if it is not in the dictionary already

        self.get_vertex(v1).adjacent_to.append(self.vertexDic[v2])
        # print(f" {adjList[i]} , {adjList[i + 1]}")
        self.get_vertex(v2).adjacent_to.append(self.vertexDic[v1])

        # if v1 not in self.vertexDic.keys():
        #     self.add_vertex(v1)
        # elif v2 not in self.vertexDic.keys():
        #     self.add_vertex(v2)
        #
        # # Add to adjacency list
        # if v2 not in Vertex(v1, None, False).adjacent_to:
        #     Vertex(v1, None, False).adjacent_to.append(v2)
        # if v1 not in Vertex(v2, None, False).adjacent_to:
        #     Vertex(v2, None, False).adjacent_to.append(v1)

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order
           Note: Results of Python sort on the list satisifies ascending order requirement'''
        # print(f"vertices: {self.vertices}")
        v = sorted(self.vertices)
        # print(v)
        return v

    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list should contain the 
           vertices (in 'Python List Sort' order) in the connected component represented by that list.
           The overall list of lists should also be in order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        s = Stack(len(self.vertices))
        totalList = []
        for ver in self.vertexDic:
            # print(ver)
            # print(self.vertexDic)
            # print(self.vertexDic[ver])
            conn_comp = []
            if self.vertexDic[ver].visited is False:
                s.push(self.vertexDic[ver])
                while not s.is_empty():
                    v = s.pop()
                    # print(self.vertices[v])
                    # print(v)
                    if v.visited is False:
                        v.visited = True
                        conn_comp.append(v.id)
                        # print(conn_comp)
                        # print(f" 5: {v.adjacent_to}")
                    for vertex in v.adjacent_to:
                        vert = vertex.id
                        # print(f" v: {self.vertexDic[vertex]}")
                        # print(vert)
                        if self.vertexDic[vert].visited is False:
                            # print('run')
                            s.push(v)
                            s.push(vertex)
                            break
                    totalList.sort()
                totalList.append(conn_comp)

        for item in totalList:
            # print(item)
            item.sort()

        return totalList

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        # start = Vertex('start', None, False)
        vertQueue = Queue(len(self.vertices))
        for i in range(len(self.vertices)):

            if self.vertexDic[self.vertices[i]].color is None:
                self.vertexDic[self.vertices[i]].color = 'white'
            # print(f"1: {self.vertexDic[self.vertices[i]]}")
            vertQueue.enqueue(self.vertexDic[self.vertices[i]])
            while not vertQueue.is_empty():
                ver = vertQueue.dequeue()
                # print(f"ver color: {self.vertexDic[ver].id},{self.vertexDic[ver].color}")
                # print(ver)
                # print(f"adj: {ver.adjacent_to}")
                for a in ver.adjacent_to:
                    print(f"color: {a.id},{a.color}")
                    if a.color is None:
                        # print(f"a: {a}")
                        if ver.color == 'black':
                            a.color = 'white'
                            vertQueue.enqueue(ver)
                        elif ver.color == 'white':
                            a.color = 'black'
                            vertQueue.enqueue(ver)
                    elif a.color == ver.color:
                        return False
        return True
