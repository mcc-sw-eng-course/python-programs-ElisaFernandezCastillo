
class Board:


    def __init__(self, *args, **kwargs):
        self.size_x = 8
        self.size_y = 8
        
        #esta madre no funciona tan cool
        self.square = [[None] * self.size_x for i in range(self.size_y)]

        for i in range(self.size_y):
            for j in range(self.size_y):
                self.square[i][j] = {
                    "piece": None
                }

    def get_piece(self, x, y):
        return self.square[x][y]["piece"]

    def set_piece(self, x, y, piece):
        self.square[x][y]["piece"] = piece

