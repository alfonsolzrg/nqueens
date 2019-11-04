import copy

class NQueensBoard():
  """N - Queen problem solver"""

  def __init__(self, board_size):
    """
    Initialize the board. 0 means there is no queen in the square, 
    1 the opposite.
    """
    self._board = [[0] * board_size for _ in range(board_size) ]
    self.board_size = board_size
    self.solutions = []

  def unset_queen(self, row, col):
    self._board[row][col] = 0

  def set_queen(self, row, col):
    self._board[row][col] = 1

  def get_solutions(self):
    self.place_queens(0)
    return self.solutions

  def place_queens(self, col):
    # Base case: we placed a queen at the last col, so we found a solution.
    if col == self.board_size:
      print("Found a solution! -> \n{}".format(self))
      self.solutions.append(copy.deepcopy(self._board))
      return True

    success = False
    for row in range(self.board_size):
      if(self.is_safe_from_attack(row, col)):
        # Place the queen here
        self.set_queen(row, col)
        success = self.place_queens(col + 1) or success
        # Now, backtrack: unset the queen and try a different position.
        self.unset_queen(row, col)
    return success

  def is_safe_from_attack(self, row, col):
    """
    Checks if a (row, col) position is safe from being attacked by another
    queen. Runtime complexity: O(3N)
    """
    # If there is another queen in this row or col, it's not safe.
    for i in range(self.board_size):
      if self._board[row][i] == 1 or self._board[i][col] == 1:
        return False

    # Now, check the two diagonals.
    # 1st diagonal \ - we can show that the position (n, m) we need to check
    # corresponds to the following formula:
    # m = n + col - row
    for n in range(self.board_size):
      m = n + col - row
      if m > self.board_size - 1 or m < 0: # Hit the edge
        continue
      if self._board[n][m] == 1:
        return False

    # 2nd diagonal / - we can show that the position (n, m) we need to check
    # corresponds to the following formula:
    # m = col + row - n
    for n in range(self.board_size):
      m = col + row - n
      if m > self.board_size - 1 or m < 0: # Hit the edge
        continue
      if self._board[n][m] == 1:
        return False

    return True

  def get_board(self):
    return self._board

  def __repr__(self):
    return str('\n'.join([str(row) for row in self._board]))
