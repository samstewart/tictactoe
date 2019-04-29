import unittest
from tic_tac_toe import *
from copy import deepcopy 

class TicTacToeTest(unittest.TestCase):
    def test_check_win_test(self):
        self.assertEqual(check_win([[1, 0, 0], [1, 0, 0], [1, 0, 0]], range(3), [0, 0, 0]), 1)
        self.assertEqual(check_win([[-1, 0, 0], [1, 0, 0], [1, 0, 0]], range(3), [0,0,0]), 0)
        self.assertEqual(check_win([[-1, 0, 0], [0, -1, 0], [0, 0, -1]], range(3), range(3)), -1)
        self.assertEqual(check_win([[-1, 0, 0], [1, 0, 0], [1, 0, 0]], range(3), range(3)), 0)

    def test_who_wins_test(self):
        self.assertEqual(who_wins([[1, 0, 0], [1, 0, 0], [1, 0, 0]]), 1)
        self.assertEqual(who_wins([[-1, 0, 0], [1, 0, 0], [1, 0, 0]]), 0)
        self.assertEqual(who_wins([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]), -1)
        self.assertEqual(who_wins([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 1)
        self.assertEqual(who_wins([[1, 1, 1], [0, 1, 0], [1, 0, 0]]), 1)
        self.assertEqual(who_wins([[1, 1, 1], [0, 1, 0], [1, 0, 0]]), 1)

    def test_all_possible_boards_test(self):
        gen = all_possible_boards([[1, 0], [0, 1]], 1)
        self.assertEqual(gen.next(), [[1, 1], [0, 1]])
        self.assertEqual(gen.next(), [[1, 0], [1, 1]])

        gen = all_possible_boards([[0, 0, 0], [1, 0, 0], [1, 0, 0]], 1)
        self.assertEqual(gen.next(), [[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        self.assertEqual(gen.next(), [[0, 1, 0], [1, 0, 0], [1, 0, 0]])



    def test_oponent_test(self):
        self.assertEqual(opponent(1), -1)
        self.assertEqual(opponent(-1), 1)

    def test_argmax(self):
        self.assertEqual(argmax([1,2, -1]), 1)
    def test_argmin(self):
        self.assertEqual(argmin([1,2, -1]), 2 )



    def test_board_is_full_test(self):
        # test on smaller board, just for convenience
        self.assertTrue(board_is_full([[1, 1], [-1, -1]]))
        self.assertFalse(board_is_full([[0, 1], [-1, -1]]))


    def test_score_move(self):
        self.assertEqual(score_move([[1, 0, 0], [1, -1, 0], [1, 0, 0]], 1), 1)
        self.assertEqual(score_move([[0, 0, 0], [-1, 0, 0], [-1, 0, 0]], 1), -1)
        self.assertEqual(score_move([[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]], 1), -1)

       
    def test_check_if_game_over_test(self):
        self.assertTrue(check_if_game_over([
            [1, 0, 0], 
            [1, 0, 0], 
            [1, 0, 0]]))
        self.assertFalse(check_if_game_over([
            [0, 0, 0], 
            [1, 0, 0], 
            [1, 0, 0]]))

if __name__ == '__main__':
#    suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest) 
    suite  = unittest.TestSuite()
    suite.addTest(TicTacToeTest('test_check_win_test'))
    suite.addTest(TicTacToeTest('test_who_wins_test'))
    suite.addTest(TicTacToeTest('test_all_possible_boards_test'))
    suite.addTest(TicTacToeTest('test_oponent_test'))
    suite.addTest(TicTacToeTest('test_board_is_full_test'))
    suite.addTest(TicTacToeTest('test_check_if_game_over_test'))
    suite.addTest(TicTacToeTest('test_argmax'))
    suite.addTest(TicTacToeTest('test_argmin'))
    suite.addTest(TicTacToeTest('test_score_move'))
    unittest.TextTestRunner(verbosity=2).run(suite)
