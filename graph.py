class Node:

    def __init__(self, idx, data=0) -> None:
        self.id = idx
        self.data = data
        self.connectedTo = list()
    
    def addNeighbour(self, neighbour):
        if neighbour.id not in self.connectedTo:
            self.connectedTo.append(neighbour.id)

    def setData(self, data):
        self.data = data
    
    def getConnections(self):
        return self.connectedTo
    
    def getID(self):
        return self.id
    
    def getData(self):
        return self.data
    
    def __str__(self) -> str:
        return str(self.data) + " Connected to: " + str([x.data for x in self.connectedTo])

class Graph:
    n = 0

    def __init__(self) -> None:
        self.nodes = dict()
    
    def addNode(self, idx):
        if idx in self.nodes:
            return None
        
        Graph.n += 1
        node = Node(idx=idx)
        self.nodes[idx] = node
        return node
    
    def addNodeData(self, idx, data):
        if idx in self.nodes:
            node = self.nodes[idx]
            node.setData(data)
        else:
            print("No ID to add the data.")
    
    def addEdge(self, src, dst):
        self.nodes[src].addNeighbour(self.nodes[dst])
        self.nodes[dst].addNeighbour(self.nodes[src])
    
    def isNeighbour(self, u, v):
        return v in self.nodes[u].getConnections()
    
    def printEdges(self):
        for idx in self.nodes:
            node = self.nodes[idx]
            for connection in node.getConnections:
                print(node.getID(), " --> ", self.nodes[connection].getID())
    
    def getNode(self, idx):
        if idx in self.nodes:
            return self.nodes[idx]
        return None
    
    def getAllNodeIds(self):
        return self.nodes.keys()
