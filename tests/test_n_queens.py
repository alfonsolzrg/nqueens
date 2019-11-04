from unittest import TestCase

from ..n_queens import NQueensSolver


class TestNQueensSolver(TestCase):
  """This tests the individual methods of the n-queens solver"""

  def test_if_placement_is_safe_from_attack(self):
    solver = NQueensSolver(3)
    solver.set_queen(0, 0)

    # Test placement on same row
    self.assertFalse(solver.is_safe_from_attack(0, 1))

    # Test placement on same col
    self.assertFalse(solver.is_safe_from_attack(1, 0))

    # Test placement on diagonal \
    self.assertFalse(solver.is_safe_from_attack(1, 1))

    # Test placement on diagonal /
    solver.unset_queen(0, 0)
    solver.set_queen(2, 2)
    self.assertFalse(solver.is_safe_from_attack(0, 0))

  def test_it_finds_simple_solution_for_n_equals_1(self):
    solver = NQueensSolver(1)
    solutions = solver.get_solutions()
    self.assertEqual(1, len(solutions))
    solution_solver = NQueensSolver(1)
    solution_solver.set_queen(0, 0)
    self.assertEqual(solutions.pop(), solution_solver.get_board())

  def test_it_finds_no_solution_for_n_equals_2(self):
    solver = NQueensSolver(2)
    solutions = solver.get_solutions()
    self.assertEqual(0, len(solutions))

  def test_it_finds_no_solution_for_n_equals_3(self):
    solver = NQueensSolver(3)
    solutions = solver.get_solutions()
    self.assertEqual(0, len(solutions))

  def test_it_finds_all_2_solutions_for_n_equals_4(self):
    solver = NQueensSolver(4)
    solutions = solver.get_solutions()
    self.assertEqual(2, len(solutions))

  def test_it_finds_all_92_solutions_for_n_equals_8(self):
    solver = NQueensSolver(8)
    solutions = solver.get_solutions()
    self.assertEqual(92, len(solutions))

  def test_it_finds_all_352_solutions_for_n_equals_9(self):
    solver = NQueensSolver(9)
    solutions = solver.get_solutions()
    self.assertEqual(352, len(solutions))
