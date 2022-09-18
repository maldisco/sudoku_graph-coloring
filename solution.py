from sudoku import Sudoku


class Solution:

    def __init__(self) -> None:
        self.board: list[int][int] = self.getBoard()
        self.sudoku: Sudoku = Sudoku()
        self.mappedGrid: list[int][int] = self.sudoku.getGridMatrix()

    def initialize(self):
        """ Initialize numbers pre-generated

        Returns:
            list[int]: a list that describes the board
            list[int]: a list that tells what cells were already given
        """

        color = [0] * (self.sudoku.graph.n+1)
        given = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    idx = self.mappedGrid[row][col]
                    color[idx] = self.board[row][col]
                    given.append(idx)

        return color, given

    def solve(self, m: int = 9):
        """ Apply the algorithm to solve

        Args:
            m (int, optional): number of colors. Defaults to 9.

        Returns:
            list[int]: solved sudoku board
        """
        color, given = self.initialize()
        if (self.__solve(m, color, 1, given) is None):
            print("This board could not be solved.")
            return False

        count = 1
        for row in range(9):
            for col in range(9):
                self.board[row][col] = color[count]
                count += 1

        return color

    def __solve(self, m: int, color: list[int], v: int, given: list[int]):
        """ Recursive function that fills the cells

        Args:
            m (int): number of colors (or numbers is this case)
            color (list[int]): the board
            v (int): current vertex
            given (list[int]): cells pre-generated

        Returns:
            bool: success
        """
        if v == self.sudoku.graph.n+1:
            return True

        for c in range(1, m+1):
            if self.__check(v, color, c, given):
                color[v] = c
                if self.__solve(m, color, v+1, given):
                    return True

            if v not in given:
                color[v] = 0

    def __check(self, v: int, color: list[int], c: int, given: list[int]):
        """ Check if a cell V can hold a number C

        Args:
            v (int): cell
            color (list[int]): board
            c (int): color
            given (list[int]): filled cells

        Returns:
            bool: True if can
        """
        if v in given and color[v] == c:
            return True
        elif v in given:
            return False

        for i in range(1, self.sudoku.graph.n+1):
            if color[i] == c and self.sudoku.graph.isNeighbour(v, i):
                return False
        return True

    def getBoard(self):
        """ Generate a (not yet) random initial state of the board

        Returns:
            list[int][int]: 9x9 matrix
        """

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
        """ Print current state of the board
        """
        for i in range(len(self.board)):
            if i % 3 == 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])):
                if j % 3 == 0:
                    print(" |  ", end="")
                if j == 8:
                    print(self.board[i][j] if self.board[i][j] != 0 else ' ', " | ")
                else:
                    print(f"{ self.board[i][j] if self.board[i][j] != 0 else ' ' } ", end="")
        print("  - - - - - - - - - - - - - - ")
