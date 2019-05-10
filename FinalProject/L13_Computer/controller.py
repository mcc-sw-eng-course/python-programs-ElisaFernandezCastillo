from piece import CheckerPiece 
from board import Board 
import time

class CheckersController:
    pieces = []
    def placePiece(self, piece, x, y):   
        self.board.set_piece(x, y, piece)

    def buildPiece(self):
        return {
            "owner":None, 
            "type":"peon",
            "index":None            
        }

    def __init__(self):
        self.board = Board()
        self.current_player = 1 #*
        self.opponent_player=2#*
        self.computer_player=2 #** these parameters will be changed by the user once s/he selects which pieces s/he wants
        self.player_jumped=False
        self.computer_jumped_player=False
        self.win=False
        self.draw=False
        self.winner=0 #Player (number)who is the winner
        self.current_player_pieces=None
        self.opponent_player_pieces=None
        self.current_player_available_moves=None
        self.opponent_player_available_moves =None

        for a in range(12):
            piece = self.buildPiece()
            piece["owner"] = 1
            piece["index"] = len(self.pieces)
            self.pieces.append(piece)
        
        for a in range(12):
            piece = self.buildPiece()
            piece["owner"] = 2
            piece["index"] = len(self.pieces)
            self.pieces.append(piece)

        self.placePiece(self.pieces[0], 1, 0)
        self.placePiece(self.pieces[1], 3, 0)
        self.placePiece(self.pieces[2], 5, 0)
        self.placePiece(self.pieces[3], 7, 0)
        self.placePiece(self.pieces[4], 0, 1)
        self.placePiece(self.pieces[5], 2, 1)
        self.placePiece(self.pieces[6], 4, 1)
        self.placePiece(self.pieces[7], 6, 1)
        self.placePiece(self.pieces[8], 1, 2)
        self.placePiece(self.pieces[9], 3, 2)
        self.placePiece(self.pieces[10], 5, 2)
        self.placePiece(self.pieces[11], 7, 2)

        self.placePiece(self.pieces[12], 0, 7)
        self.placePiece(self.pieces[13], 2, 7)
        self.placePiece(self.pieces[14], 4, 7)
        self.placePiece(self.pieces[15], 6, 7)
        self.placePiece(self.pieces[16], 1, 6)
        self.placePiece(self.pieces[17], 3, 6)
        self.placePiece(self.pieces[18], 5, 6)
        self.placePiece(self.pieces[19], 7, 6)
        self.placePiece(self.pieces[20], 0, 5)
        self.placePiece(self.pieces[21], 2, 5)
        self.placePiece(self.pieces[22], 4, 5)
        self.placePiece(self.pieces[23], 6, 5)

    #just a function to visualize the board
    def printSimple(self):
        board_string = ""
        for i in range(self.board.size_x):
            for j in range(self.board.size_y):
                content = " "
                piece = self.board.get_piece(j, i)

                if piece:
                    content = piece["owner"]
                board_string=board_string + "["+str(content)+"]"
            
            board_string=board_string + "\n"
        #print (board_string)
        return board_string


    def check_num_pieces(self, player):

        board=self.printSimple()
        num_pieces=board.count(player)
        return num_pieces


    def check_num_possible_moves(self):

        self.current_player_available_moves=self.get_available_moves_player(self.current_player)
        self.opponent_player_available_moves=self.get_available_moves_player(self.opponent_player)
        # if current player's moves are empty and opponent player's moves are empty (i.e. there are no moves left in the game)
        if((not self.current_player_available_moves)and (not self.opponent_player_available_moves)):
            self.draw=True

        else:
            # if current player's moves are empty  (i.e.  current player is left with no moves)
            if (not self.current_player_available_moves):
                self.win=True
                self.winner=self.opponent_player

    # returns a list of tuples with all the coordinates of the player's pieces
    def get_available_pieces_player(self,current_player):
        current_player_pieces_coordinates=[]
        for i in range(self.board.size_x):
            for j in range(self.board.size_y):
                current_piece=self.board.get_piece(j,i)
                if (current_piece and (current_piece["owner"]==current_player)):
                    coordinates=(j,i)
                    current_player_pieces_coordinates.append(coordinates)
        return current_player_pieces_coordinates

    # returns a list of tuples with all possible moves and jumps  for current player
    def get_available_moves_player(self,current_player):
        available_moves=[]
        available_coordinates=self.get_available_pieces_player(current_player)
        for i in range(len(available_coordinates)):
            coordinate=available_coordinates[i]
            moves=self.available_moves(coordinate[0],coordinate[1])
            for j in range(len(moves)):
                if(moves[j]):
                    available_moves.append(moves[j])
            jumps=self.available_jumps(coordinate[0],coordinate[1])
            for k in range(len(jumps)):
                if(jumps[k]):
                    available_moves.append(jumps[k])
        return available_moves

    #This function is used only for the moves done by the computer. First, it takes  in consideration ONLY the possible jumps. If there are no jumps, it will consider moves
    def get_available_jumps_or_moves_player(self,current_player):
        available_moves=[]
        available_coordinates=self.get_available_pieces_player(current_player)
        for i in range(len(available_coordinates)):
            coordinate=available_coordinates[i]
            jumps = self.available_jumps(coordinate[0], coordinate[1])
            for k in range(len(jumps)):
                if (jumps[k]):
                    available_moves.append(jumps[k])
                    self.computer_jumped_player = True
        if (not available_moves):
            for l in range(len(available_coordinates)):
                coordinate = available_coordinates[l]
                moves=self.available_moves(coordinate[0],coordinate[1])
                for j in range(len(moves)):
                    if(moves[j]):
                        available_moves.append(moves[j])
        return available_moves


    def move_is_valid(self, source_x, source_y, dest_x, dest_y):

        if (not self.check_piece_exist(source_x, source_y, dest_x, dest_y)):
            return False

        if (self.player_jumped):
            return False

        if (not self.check_inbounds(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_square_not_busy(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_can_move(source_x, source_y, dest_x, dest_y) ):
            return False
  
        return True

    def jump_is_valid(self, source_x, source_y, dest_x, dest_y):
        if (not self.check_piece_exist(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_inbounds(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_square_not_busy(source_x, source_y, dest_x, dest_y)):
            return False


        if (not self.check_can_jump(source_x, source_y, dest_x, dest_y)):
            return False
        return True

    def check_piece_exist(self, source_x, source_y, dest_x, dest_y):
        #print ("Check piece exist")
        source_piece = self.board.get_piece(source_x, source_y)
        if (not source_piece):
            #print ("Invalid move, there isnt even a piece in the source square")
            return False
        return True 

    def check_inbounds(self, source_x, source_y, dest_x, dest_y):
        #print ("Check inbounds")
        #check in bounds
        if ((dest_x < 0 or dest_y < 0 or dest_x >= self.board.size_x or dest_y >= self.board.size_y) ):
            #print ("Invalid move, piece will fall out of bounds")
            return False
        return True 

    def check_square_not_busy(self, source_x, source_y, dest_x, dest_y):
        #print ("Check not busy")
        #check quare not already busy
        dest_piece = self.board.get_piece(dest_x, dest_y)
        if (dest_piece != None):
            #print("Invalid move, destination square is alredy occupied")
            return False
        return True

    def check_can_move(self, source_x, source_y, dest_x, dest_y):
        #print ("Check can move")

        source_piece = self.board.get_piece(source_x, source_y)
        #check if can move
        if (source_piece["owner"] == 1):
            if (dest_y == source_y + 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) ):
                return True

        if (source_piece["owner"] == 2):
            if (dest_y == source_y - 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) ):
                return True

        if (source_piece["type"] == "king"):
            if ((dest_y == source_y + 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) )
            or   (dest_y == source_y - 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) )):
                return True

        #print("Invalid move")
        return False
    
    def check_can_jump(self, source_x, source_y, dest_x, dest_y):
        #print ("Check can jump")
        source_piece = self.board.get_piece(source_x, source_y)
        #check if can jump

        #TODO: Clean duplicated code
        if (source_piece["owner"] == 1 or source_piece["type"]=="king"):
            if (dest_y == source_y + 2 and dest_x == source_x -2  ):
                jumped_piece = self.board.get_piece(source_x -1 , source_y +1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

            if (dest_y == source_y + 2 and dest_x == source_x +2  ):
                jumped_piece = self.board.get_piece(source_x +1, source_y +1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True
                

        if (source_piece["owner"] == 2 or source_piece["type"]=="king"):
            if (dest_y == source_y - 2 and dest_x == source_x -2  ):
                jumped_piece = self.board.get_piece(source_x -1 , source_y -1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

            if (dest_y == source_y - 2 and dest_x == source_x +2  ):
                jumped_piece = self.board.get_piece(source_x +1 , source_y -1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

        #print("Invalid jump")
        return False
            
    def move_piece(self, source_x, source_y, dest_x, dest_y):

        current_player_available_jumps=self.available_jumps(source_x,source_y)

        #if there are jumps available, piece should jump instead of moving
        if (self.move_is_valid(source_x, source_y, dest_x, dest_y) and (not current_player_available_jumps)):
            self.board.set_piece(dest_x, dest_y, self.board.get_piece(source_x, source_y))
            self.board.set_piece(source_x, source_y, None) #source square is left without piece
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 1 and dest_y == 7):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 2 and dest_y == 0):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"

            self.current_player = 2 if self.current_player == 1 else 1
            if (self.current_player==2):
                self.opponent_player=1
            else:
                self.opponent_player = 2

        if (self.jump_is_valid(source_x, source_y, dest_x, dest_y)):
            self.board.set_piece(dest_x, dest_y, self.board.get_piece(source_x, source_y))
            self.board.set_piece(int((dest_x+source_x)/2), int((dest_y+source_y)/2), None) #opponent's piece is eliminated
            self.board.set_piece(source_x, source_y, None) #source square is left without piece
            self.player_jumped=True
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 1 and dest_y == 7):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 2 and dest_y == 0):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"

            if (not self.available_jumps(dest_x, dest_y)):
                self.current_player = 2 if self.current_player == 1 else 1
                if (self.current_player == 2):
                    self.opponent_player = 1
                else:
                    self.opponent_player = 2
                self.player_jumped = False

    def available_moves(self, source_x, source_y):
        available_moves_list = []
        available_moves_list = available_moves_list + self.get_available_moves(source_x, source_y)

        return available_moves_list
    

    def available_jumps(self, source_x, source_y):
        available_jumps_list = []
        available_jumps_list = available_jumps_list + self.get_available_jumps(source_x, source_y)

        return available_jumps_list


    #gets available moves (not jumps) for a given square (if a piece is there)
    #returns a list of tuples
    def get_available_moves(self, x, y):
        piece = self.board.get_piece(x, y)
        possible_destinations = []
        available_moves = []
        if (not piece):
            return []
        
        possible_destinations.append( (x+1, y+1) )
        possible_destinations.append( (x-1, y+1) )
        possible_destinations.append( (x+1, y-1) )
        possible_destinations.append( (x-1, y-1) )

        for dest in possible_destinations:
        #    print ("Checking move is valid", x, y, dest[0], dest[1])
            if (self.move_is_valid(x, y, dest[0], dest[1])):
                available_moves.append(  (x, y, dest[0], dest[1])  )

        return available_moves

    #gets available moves (not jumps) for a given square (if a piece is there)
    #returns a list of tuples
    def get_available_jumps(self, x, y):
        piece = self.board.get_piece(x, y)

        possible_destinations = []
        available_jumps = []
        if (not piece):
            return []
        
        possible_destinations.append( (x+2, y+2) )
        possible_destinations.append( (x-2, y+2) )
        possible_destinations.append( (x+2, y-2) )
        possible_destinations.append( (x-2, y-2) )

        for dest in possible_destinations:
            if (self.jump_is_valid(x, y, dest[0], dest[1])):
                available_jumps.append( (x, y, dest[0], dest[1]) )

        return available_jumps


