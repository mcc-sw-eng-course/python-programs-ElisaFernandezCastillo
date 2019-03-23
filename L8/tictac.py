import tictacBoard
import math
from random import randint

class Tictac:
    def __init__(self):
        self.board = tictacBoard.TictacBoard()
        self.player_mark = ["O", "X"]
        self.players = 2
        self.current_player=0
        self.computer_player_enabled=True
        self.computer_player_turn = 1


    def main_loop(self):
        self.board.draw_tictac()
        if (self.computer_player_enabled and self.current_player == self.computer_player_turn):
            print("Waiting for computer selection...")
            #call algorithm for computer player
            coord_input = self.computer_select_random()  
        else:
            coord_input =self.request_mark_input("Player {} turn, please enter a location to mark (1-9)\n".format(self.player_mark[self.current_player]))
        
        self.board.set_state(coord_input[0], coord_input[1], self.player_mark[self.current_player])
        
        if (self.board.check_win(self.player_mark[0])):
            self.board.draw()
            print ("Player {} wins!".format(self.player_mark[0]))
        elif(self.board.check_win(self.player_mark[1])):
            self.board.draw()
            print ("Player {} wins!".format(self.player_mark[1]))
        elif(self.board.check_tie()):
            self.board.draw()
            print ("The game ends in a tie!")
        else:
            self.current_player = (self.current_player + 1) % 2
            self.main_loop()


    def computer_select_random(self):
        available_coords = self.board.get_available_coords()
        coord_input = available_coords[randint(0, len(available_coords)-1) ]
        return coord_input

    def location_to_coord(self, location):
        y = math.floor((location-1) / 3)
        x = ((location - 1) % 3)
        return [x, y]

    def request_mark_input(self, message):
        location_input = input (message)
        try:
            location_input = int(location_input)
        except ValueError:
            return self.request_mark_input("Location is invalid, please enter an integer number from 1 to 9\n")

        if (location_input < 0 or location_input > 9):
            return self.request_mark_input("Location is invalid, please enter an integer number from 1 to 9\n")

        coord = self.location_to_coord(location_input)
        if (self.board.get_state(coord[0], coord[1])!=self.board.default_state):
            return self.request_mark_input("That location is already marked, please select a different one\n")
        return coord
