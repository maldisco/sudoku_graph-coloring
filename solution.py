from mimetypes import init
from sudoku import Sudoku


class Solution:

    def __init__(self) -> None:

        self.board = self.getBoard()
        self.graph = Sudoku()
        self.mappedGrid = self.__getMappedMatrix()

    def initialize(self):
        color = [0] * (self.graph.graph.n+1)
        given = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    idx = self.mappedGrid[row][col]
                    color[idx] = self.board[row][col]
                    given.append(idx)

        return color, given

    def solve(self, m=9):
        color, given = self.initialize()
        if (self.__solve(m, color, 1, given) is None):
            print(":(")
            return False

        count = 1
        for row in range(9):
            for col in range(9):
                self.board[row][col] = color[count]
                count += 1

        return color

    def __solve(self, m, color, v, given):
        if v == self.graph.graph.n+1:
            return True

        for c in range(1, m+1):
            if self.__check(v, color, c, given):
                color[v] = c
                if self.__solve(m, color, v+1, given):
                    return True

            if v not in given:
                color[v] = 0
    
    def __check(self, v, color, c, given):
        if v in given and color[v] == c:
            return True
        elif v in given:
            return False

        for i in range(1, self.graph.graph.n+1):
            if color[i] == c and self.graph.graph.isNeighbour(v, i):
                return False
        return True

    def __getMappedMatrix(self):
        matrix = [[0 for cols in range(9)]
                  for rows in range(9)]

        count = 1
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = count
                count += 1
        return matrix

    def getBoard(self):

        board = [
            [8, 0, 0, 1, 5, 0, 6, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 4, 1],
            [5, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 9, 0, 6, 2],
            [0, 0, 0, 0, 3, 0, 0, 0, 0],
            [1, 4, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 9],
            [2, 9, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 5, 0, 9, 7, 0, 0, 6]
        ]

        return board

    def printBoard(self):
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)):
            if i % 3 == 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])):
                if j % 3 == 0:
                    print(" |  ", end="")
                if j == 8:
                    print(self.board[i][j], " | ", i+1)
                else:
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")
