from unittest import TestCase

from ..n_queens import NQueensBoard


class TestNQueensProblem(TestCase):
  """This tests the individual methods of the n-queens solver"""

  def test_if_placement_is_safe_from_attack(self):
    board = NQueensBoard(3)
    board.set_queen(0, 0)

    # Test placement on same row
    self.assertFalse(board.is_safe_from_attack(0, 1))

    # Test placement on same col
    self.assertFalse(board.is_safe_from_attack(1, 0))

    # Test placement on diagonal \
    self.assertFalse(board.is_safe_from_attack(1, 1))

    # Test placement on diagonal /
    board.unset_queen(0, 0)
    board.set_queen(2, 2)
    self.assertFalse(board.is_safe_from_attack(0, 0))

  def test_it_finds_simple_solution_for_n_equals_1(self):
    board = NQueensBoard(1)
    solutions = board.get_solutions()
    self.assertEqual(1, len(solutions))
    solution_board = NQueensBoard(1)
    solution_board.set_queen(0, 0)
    self.assertEqual(solutions.pop(), solution_board.get_board())

  def test_it_finds_no_solution_for_n_equals_2(self):
    board = NQueensBoard(2)
    solutions = board.get_solutions()
    self.assertEqual(0, len(solutions))

  def test_it_finds_no_solution_for_n_equals_3(self):
    board = NQueensBoard(3)
    solutions = board.get_solutions()
    self.assertEqual(0, len(solutions))

  def test_it_finds_all_2_solutions_for_n_equals_4(self):
    board = NQueensBoard(4)
    solutions = board.get_solutions()
    self.assertEqual(2, len(solutions))

  def test_it_finds_all_92_solutions_for_n_equals_8(self):
    board = NQueensBoard(8)
    solutions = board.get_solutions()
    self.assertEqual(92, len(solutions))

  def test_it_finds_all_352_solutions_for_n_equals_9(self):
    board = NQueensBoard(9)
    solutions = board.get_solutions()
    self.assertEqual(352, len(solutions))
