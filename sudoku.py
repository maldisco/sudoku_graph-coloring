from graph import Graph

class Sudoku:
    """ This class holds a sudoku board and a graph representing it
    """


    def __init__(self) -> None:
        self.graph = Graph()
        self.rows = 9
        self.cols = 9
        self.total_blocks = self.rows * self.cols
    
        self.__generateGraph()
        self.connectEdges()
        self.allIds = self.graph.getAllNodeIds()
    
    def __generateGraph(self):
        """ Generate the basic graph (all 81 nodes)
        """

        for idx in range(1, self.total_blocks+1):
            self.graph.addNode(idx)
    
    def connectEdges(self) : 
        """ connect vertex in the same row, column or 3x3 grid
        """
        matrix = self.getGridMatrix()

        head_connections = dict()

        for row in range(9) :
            for col in range(9) : 
                
                head = matrix[row][col]
                connections = self.__findConnections(matrix, row, col)
                
                head_connections[head] = connections

        self.__connect(head_connections)
        
    def __connect(self, head_connections : dict) : 
        """ Connect the nodes 

        Args:
            head_connections (dict): a dict of dicts that hold all connections in the board
        """
        for head in head_connections.keys() : 
            connections = head_connections[head]
            for key in connections :
                for v in connections[key] : 
                    self.graph.addEdge(src=head, dst=v)
 
    def __findConnections(self, matrix : list[int], rows : int, cols : int) :
        """ Find out what cells will be connected to the cell in given row and col

        Args:
            matrix (list[int][int]): board
            rows (int): cell row
            cols (int): cell col

        Returns:
            dict: cells to connect
        """
        connections = dict()

        row = []
        col = []
        block = []
    
        for c in range(cols+1, 9) : 
            row.append(matrix[rows][c])
        
        connections["rows"] = row

        for r in range(rows+1, 9):
            col.append(matrix[r][cols])
        
        connections["cols"] = col
        
        if rows%3 == 0 : 

            if cols%3 == 0 :
                
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])

        elif rows%3 == 1 :
            
            if cols%3 == 0 :
                
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])

        elif rows%3 == 2 :
            
            if cols%3 == 0 :
                
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
        
        connections["blocks"] = block
        return connections

    def getGridMatrix(self) : 
        """
        Generates the 9x9 grid or matrix consisting of node ids.
        
        This matrix will act as amapper of each cell with each node 
        through node ids
        """
        matrix = [[0 for cols in range(self.cols)] 
        for rows in range(self.rows)]

        count = 1
        for rows in range(9) :
            for cols in range(9):
                matrix[rows][cols] = count
                count+=1
        return matrix
