from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base


def get_engine(db_username, db_password, db_host, db_name, **kwargs):
  return create_engine('postgresql://{}:{}@{}/{}'.format(
    db_username,
    db_password,
    db_host,
    db_name
  ), **kwargs)

Base = declarative_base()

class NQueensBoard(Base):
  """
  This class saves the solutions to the N-Queens problem as PostgreSQL's Array
  data type.
  """
  __tablename__ = 'solutions'

  board_size = Column("board_size", Integer, primary_key=True)
  solutions = Column("solutions", postgresql.ARRAY(Integer))

  def __repr__(self):
    return 'Board size: {}, solutions found: {}'.format(
      self.board_size,
      len(self.solutions)
    )
