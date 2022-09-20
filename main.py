from solution import Solution

# https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072

s = Solution()
print("INITIAL STATE OF THE BOARD: \n")
s.printBoard()
print("Solving ...")
s.solve(m=9)
print("\nSuccess!")
print("FINAL STATE OF THE BOARD: ")
s.printBoard()