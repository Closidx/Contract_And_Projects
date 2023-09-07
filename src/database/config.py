from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base


class Database:
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
