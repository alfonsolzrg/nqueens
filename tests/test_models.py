from pytest import fixture
from unittest import TestCase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy_utils import database_exists, create_database, drop_database

from ..models import NQueensBoard, get_engine, Base
from ..config import CONFIG


class TestModels(TestCase):
  """
  This tests that we are successfully able to read/write to PostgreSQL via
  SQLAlchemy.
  If there are problems in the connection, export the following ENV variables:

  ```
  export DB_USERNAME=myusername
  export DB_PASSWORD=mypassword
  export DB_HOST=localhost
  export DB_NAME=mydb
  ```
  """

  def setUp(self):
    self.engine = get_engine(
      CONFIG['DB_USERNAME'],
      CONFIG['DB_PASSWORD'],
      CONFIG['DB_HOST'],
      # Use a separate database to run tests, delete after running test suite.
      'test_' + CONFIG['DB_NAME'],
      poolclass=NullPool # We don't want to use db pooling for tests
    )
    if database_exists(self.engine.url):
      drop_database(self.engine.url)
    create_database(self.engine.url)

    Base.metadata.create_all(self.engine)
    Session = sessionmaker(bind=self.engine)
    self.session = Session()

  def tearDown(self):
    # This way, we can be sure that we're running each test with an empty db
    self.session.close()
    drop_database(self.engine.url)

  def test_connection_and_model_rw(self):
    BOARD_SIZE = 1
    SOLUTIONS = [[[1]]]
    board = NQueensBoard(board_size=BOARD_SIZE, solutions=SOLUTIONS)
    
    self.session.add(board)
    self.session.commit()
    saved_boards = self.session.query(NQueensBoard).all() 
    self.assertEqual(1, len(saved_boards))
    self.assertEqual(SOLUTIONS, saved_boards.pop().solutions)
