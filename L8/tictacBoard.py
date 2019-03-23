import board
class TictacBoard(board.Board):
    def __init__(self):
        super().__init__(3, 3, ' ')
        
    
    def full_row_equals(self,row,state):
        for x in range(0, self.size_x):
            if (self.get_state(x, row)!=state):
                return False
        return True

    def full_column_equals(self,column,state):
        for y in range(0, self.size_y):
            if (self.get_state(column, y)!=state):
                return False
        return True

    def diagonal_equals(self, state):
        for i in range(0, self.size_x):
            if (self.get_state(i, i)!=state):
                return False
        return True

    def antidiagonal_equals(self, state):
        for i in range(0, self.size_x):
            if (self.get_state(i, self.size_x-1 - i)!=state):
                return False
        return True

    def check_win(self, state):
        for i in range(0, self.size_x):
            if (self.full_column_equals(i, state)):
                return True
        
        for i in range(0, self.size_y):
            if (self.full_row_equals(i, state)):
                return True
        
        if (self.diagonal_equals(state)):
            return True
        
        if (self.antidiagonal_equals(state)):
            return True

        return False

    def check_tie(self):
        for i in range(0, self.size_x):
            for j in range(0, self.size_y):
                if (self.get_state(i, j) == " "):
                    return False
        return True

    def get_available_coords(self): 
        coord_list = []
        for i in range(0, self.size_x):
            for j in range(0, self.size_y):
                if (self.get_state(i, j) == self.default_state):
                    coord_list.append([i,j])
        return coord_list
                
    def draw_tictac(self):
        numRows = len(self.board)
        numColumns = len(self.board[0])
        count = 1
        for i in range(0, numRows):
            for j in range(0, numColumns):
                symbol = self.board[i][j] if self.board[i][j]!=" " else str(count)
                print(symbol, end=" | ")
                count = count + 1
            print()
            print("------------")