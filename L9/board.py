

class Board:
    def __init__(self, size_x, size_y, default_state):
        self.size_x = size_x
        self.size_y = size_y
        self.default_state = default_state
        self.board = [[default_state] * size_x for i in range(size_y)]
    
    def set_state(self, x, y, state):
        self.board[y][x] = state
        
    def get_state(self, x, y):
        return self.board[y][x]

    def draw(self):
        numRows = len(self.board)
        numColumns = len(self.board[0])
        msg=""
        for i in range(0, numRows):
            for j in range(0, numColumns):
                print(self.board[i][j], end=" | ")
                msg=msg+self.board[i][j]+" | "
            print()
            print("------------")
            msg=msg+"\n------------\n"
        return str(msg)
            

