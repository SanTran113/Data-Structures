from stack_array import *

# class vertex:
#     def __init__(self, adjacencies: List):
#         self.in_degree = 0
#         self.adjacencies = adjacencies

def tsort(vertices: List) -> str:
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    adjList = []
    adjDic = {}
    s = Stack(len(vertices))
    str = ''

    # if vertices is empty
    if vertices == []:
        raise ValueError('input contains no edges')

    # if length of vertices is odd
    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')

    # adjacency list for vertices with number of incoming edges (degree of zero) and adjacent vertices
    # adding in the vertices in order with every other two
    for v in vertices[0::2]:
        if v not in adjDic:
            adjDic[v] = [v, 0, []]
            adjList.append(v)

        # checking for  adjacency
    for v in vertices[1::2]:
        if v not in adjDic:
            adjDic[v] = [v, 0, []]

    for v in range(0, len(vertices), 2):
        adjDic[vertices[v]][2].append(vertices[v + 1])
        adjDic[vertices[v + 1]][1] += 1
    # print(f"adjDic: {adjDic}")
    # print(f"adjList: {adjList}")

    # if vertices has degree of zero push into stack
    for ele in adjList:
        if adjDic[ele][1] == 0:
            s.push(adjDic[ele])
            # adjList.remove(ele)
            del adjDic[ele]

    # print(s.items)

    count = 0
    # while stack is not empty pop vertex
    while s.is_empty() == False:
        ver = s.pop()
        # print(f"ver: {ver}")
        for a in ver[2]:
            adjDic[a][1] -= 1
            # print(f"adjDic[a]: {adjDic[a]}")
            if adjDic[a][1] == 0:
                count += 1
                s.push(adjDic[a])

        # output string
        str += ver[0] + '\n'

    print(adjDic)
    print(len(adjDic))
    print(count)

    # check if there is a cycle
    if len(adjDic) != count:
        raise ValueError("input contains a cycle")


    # print(f"str: {str}")
    return str