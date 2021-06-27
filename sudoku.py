import numpy
board=["..6.59...",
       "4....89..",
       "......74.",
       "3....7.9.",
       "52..4..67",
       ".9.2.....",
       "..1......",
       "..23....8",
       "....1.3.."]

board = np.array([[x for x in row] for row in board])

def solve(board, x=0, y=0):
    while True:
        if y == 9:
            return board
        if board[y,x] == ".":
            break
        x += 1
        if x == 9:
            x,y = 0, y+1
    for v in {*'123456789'} - (set(board[y, :]) | set(board[:, x]) | set(board[y//3*3:y//3*3+3, x//3*3:x//3*3+3].reshape(9))):
        newb = board.copy()
        newb[y,x] = v
        res = solve(newb,x,y)
        if res is not None:
            return res
    return None

b = solve(board)
print(b)
