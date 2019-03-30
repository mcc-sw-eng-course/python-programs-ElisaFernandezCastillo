import tictacBoard
import math
from random import randint
import socket
import threading
import tictac
import time
import json
import os
from subprocess import call

class Tictac:
    def __init__(self, ip = "127.0.0.1"):
        self.board = tictacBoard.TictacBoard()
        self.player_mark = ["O", "X"]
        self.players = 2
        self.current_player=-1
        self.computer_player_enabled=True
        self.computer_player_turn = 1
        self.player_number = -1
        self.connection_status = "disconnected"
        self.TCP_IP = ip
        self.TCP_PORT = 5050
        self.BUFFER_SIZE = 1024
        self.finisehd = False


    def main_loop(self):
        
        if (self.connection_status == "disconnected"):
            self.connect_server()
            self.redraw()
            
        #MESSAGE =  input("Enter command")

        if (self.connection_status == "connected"):
            self.update_status()
            self.board.draw_tictac()

        if (self.current_player == self.player_number):
            location = input("Your turn!, select a location to mark")
            self.send_mark_request(location)

        time.sleep(2)
        if (not self.finisehd):
            self.main_loop()

    def send_mark_request(self, location):
        try: 
            location = int(location)
        except ValueError:
            print ("Invalid input")
            return

        response = self.send_message({
            "message_type": "mark",
            "location":int(location),
            "player":self.player_number
        })

        if (response["message_type"]=="mark_ok"):
            self.update_status()
        elif (response["message_type"]=="mark_error"):
            if (response["error"] == "invalid"):
                print ("Your input is invalid, please enter a number from 1-9")
            elif (response["error"] == "marked"):
                print ("That location is already marked! Please select a different one")


    def update_status(self):
        state = self.send_message({
            "message_type": "state_update"
        })
        self.current_player = state["current_player"]
        if (self.board.board != state["board"]):
            self.board.board = state["board"]
            self.redraw()


        if (state["winner"] != -1 ):
            if (state["winner"]==self.player_number):

                self.board.draw()
                print ("Congratulations! You WIN!")
            else:
                self.board.draw()
                print ("Tough luck my friend, you lost")
            self.finisehd = True
        if (state["tie"] == 1 ):
            print ("Game ended in a tie!")
            self.board.draw()
            self.finisehd = True

    def clear(self):
        # check and make call for specific operating system
        _ = call('clear' if os.name == 'posix' else 'cls')

    def redraw(self):
        self.clear()
        self.board.draw_tictac()
        if (self.current_player != self.player_number and self.current_player != -1):
            print("Waiting for other player to select...")

    def connect_server(self):
        print("Connecting to server")
        response = self.send_message(
            {
                "message_type": "connect"
            }
        )
        if (response["message_type"] == "connected"):
            self.player_number = int(response["player_number"])
            self.connection_status = "connected"
            print ("Connected... I am player "+str(self.player_number))
        elif (response["message_type"]=="error"):
            print ("Server error: "+response["error_message"])
            self.connection_status = "rejected"

        
    
    def send_message(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        message = json.dumps(message)
        message = message.encode()
        s.send(message)
        #print ("Request:")
        #print (message)
        jdata = s.recv(self.BUFFER_SIZE)
        s.close()
        jdata = jdata.decode()
        data = json.loads(jdata)
        #print ("Response:")
        #print (data)
        return data

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
