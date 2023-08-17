from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        self.engine = create_engine("postgresql://root:root@localhost:5432/kuber")
        self.session = sessionmaker(bind=self.engine)


client = DBClient()
