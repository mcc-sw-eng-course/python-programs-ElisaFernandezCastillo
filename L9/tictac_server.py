import tictacBoard
import math
from random import randint
import socket
import threading
import json

class Tictac:
    def __init__(self):
        self.board = tictacBoard.TictacBoard()
        self.player_mark = ["O", "X"]
        self.players = 2
        self.current_player=0
        self.computer_player_enabled=True
        self.computer_player_turn = 1
        self.init_server_socket()
        self.players_connected =0
        self.winner = -1
        self.tie = 0

    def init_server_socket(self):
        self.bind_ip = "0.0.0.0"
        self.bind_port = 5050
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        self.server.listen(5)  # max backlog of connections
        print ('Listening on {}:{}'.format(self.bind_ip, self.bind_port))

    def receive_client_message(self, client_socket):
        request = client_socket.recv(1024)
        request = request.decode()
        request = json.loads(request)
        print ("Client request:")
        print (request)
        response = self.handle_client_message(request)
        response = json.dumps(response)
        print ("Response:")
        print (response)
        client_socket.send(response.encode())
        client_socket.close()

    def main_loop(self):
        while True:
            client_sock, address = self.server.accept()
            print ('Accepted connection from {}:{}'.format(address[0], address[1]))
            client_handler = threading.Thread(
                target=self.receive_client_message,
                args=(client_sock,)  
            )
            client_handler.start()

    def handle_client_message(self, message):
        print(message)
        if (message["message_type"] == "connect"):
            return self.handle_client_connection()
        if (message["message_type"] == "state_update"):
            return self.handle_status_update_request()
        if (message["message_type"] == "mark"):
            return self.handle_mark_request(message["location"])

    def handle_mark_request(self, location):
        validate_result = self.validate_location(location)
        if ( validate_result != "ok"):
            return {
                "message_type" : "mark_error",
                "error" : validate_result
            }
        
        self.mark_input(location)
        return {
            "message_type":"mark_ok"
        }

    def handle_status_update_request(self):
        state = {
            "current_player" : self.current_player,
            "board" : self.board.board,
            "winner":self.winner,
            "tie":self.tie
        }

        return state

    def handle_client_connection(self):
        if (self.players_connected < 2):
            response = {
                'message_type': 'connected',
                'player_number': self.players_connected
            }
            self.players_connected = self.players_connected +1
            return response
        else:
            response = {
                "message_type": "error",
                "error_message":"Server is not accepting more clients"
            }
            return response
    
    def mark_input(self, location_input):
        coord_input = self.location_to_coord(location_input)
        self.board.set_state(coord_input[0], coord_input[1], self.player_mark[self.current_player])
        self.board.draw_tictac()
        if (self.board.check_win(self.player_mark[0])):
            self.board.draw()
            print ("Player {} wins!".format(self.player_mark[0]))
            self.winner = 0
        elif(self.board.check_win(self.player_mark[1])):
            self.board.draw()
            print ("Player {} wins!".format(self.player_mark[1]))
            self.winner = 1
        elif(self.board.check_tie()):
            self.board.draw()
            self.tie = 1
            print ("The game ends in a tie!")
        else:
            self.current_player = (self.current_player + 1) % 2

    def computer_select_random(self):
        available_coords = self.board.get_available_coords()
        coord_input = available_coords[randint(0, len(available_coords)-1) ]
        return coord_input

    def location_to_coord(self, location):
        y = math.floor((location-1) / 3)
        x = ((location - 1) % 3)
        return [x, y]

    def validate_location(self, location_input):
        try:
            location_input = int(location_input)
        except ValueError:
            return "invalid"

        if (location_input < 0 or location_input > 9):
            return "invalid"

        coord = self.location_to_coord(location_input)
        if (self.board.get_state(coord[0], coord[1])!=self.board.default_state):
            return "marked"
        return "ok"
