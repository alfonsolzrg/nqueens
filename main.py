from os import environ
from sqlalchemy.orm import sessionmaker

from models import NQueensBoard, get_engine, Base
from n_queens import NQueensSolver
from config import CONFIG, logger


def get_db_session():
  engine = get_engine(
    CONFIG['DB_USERNAME'],
    CONFIG['DB_PASSWORD'],
    CONFIG['DB_HOST'],
    CONFIG['DB_NAME']
  )
  # Initialize tables
  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  return Session()

def solve_nqueens_and_save(board_size):
  session = get_db_session()
  # Don't solve it again if a solution already exists in the database.
  existing = session.query(NQueensBoard).filter_by(board_size=BOARD_SIZE).first()
  if existing:
    return existing

  solver = NQueensSolver(board_size)
  solutions = solver.get_solutions()
  
  board = NQueensBoard(board_size=board_size, solutions=solutions)
  session.add(board)
  session.commit()

  return session.query(NQueensBoard).filter_by(board_size=board_size).first()


if __name__ == "__main__":
  # Default to solving for N = 8
  BOARD_SIZE = int(environ.get('BOARD_SIZE', 8))

  board = solve_nqueens_and_save(BOARD_SIZE)
  logger.info('Solutions saved!')
  logger.info('Solutions: {}'.format(board))
