import networkx as nx

class Set(object):
    """docstring for Set"""
    def __init__(self, s = list(), r = -1):
        self.setElements = s
        self.rank = r
        if r == -1:
            self.parent = s[0]

    def __add__(self, other):
        if abs(self.rank) >= abs(other.rank):
            self.setElements.append(other.setElements)
            self.rank -= len(other.setElements)
        else:
            other.setElements.append(self.setElements)
            other.rank -= len(self.setElements)

    def __str__(self):
        return str(self.setElements)

def find(ele, allSets):
    for st in allSets:
        if ele in st.setElements:
            return (st. setElements, st.parent)
    return "Element not found"

if __name__ == '__main__':
    g = nx.Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 2)

    setOfNodes = list()
    #making singleton sets
    for node in g.nodes_iter():
        setOfNodes.append(Set(s = [node]))

    for edge in g.edges_iter():
        (a, b) = edge
        s1, p1 = find(a, setOfNodes)
        s2, p2 = find(b, setOfNodes)
        flag = False
        if p1 == p2:
            print('cycle')
            flag = True
            break
        else:
            s1 += s2

    if flag == False:
        print('No cycle')












