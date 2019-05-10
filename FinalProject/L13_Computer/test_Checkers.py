import unittest
import controller
import board
import checkersUI

class testCheckers(unittest.TestCase):

    def test_board(self):
        brd=board.Board()
        piece=brd.get_piece(0,1)
        self.assertEquals(piece,None)
        brd.set_piece(0,1,"pieza")
        piece_2=brd.get_piece(0,1)
        self.assertEquals(piece_2,"pieza")

    def test_controller(self):
        control=controller.CheckersController()
        num_pieces=control.check_num_pieces("1")
        self.assertEqual(num_pieces,12)
        control.check_num_possible_moves()
        self.assertEquals(len(control.current_player_available_moves),7)
        available_moves_current_player=control.get_available_moves_player(control.current_player)
        self.assertEquals(len(available_moves_current_player),7)
        available_jumps_moves=control.get_available_jumps_or_moves_player(control.current_player)
        self.assertEquals(len(available_jumps_moves), 7)
        piece_3=control.board.get_piece(1,2)
        piece_4=control.board.get_piece(2,2)
        control.move_piece(1,2,2,3)
        #piece_5 is in the same square piece_3 used to be
        piece_5=control.board.get_piece(1,2)
        self.assertEqual(piece_5,None)
        control.move_piece(4, 5, 3, 4)
        control.move_piece(2, 3, 4, 5)
        self.assertEqual(control.board.get_piece(2,3),None)


