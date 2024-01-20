from pydantic import BaseModel


class DBConfig(BaseModel):
    db_url: str
    db_username: str
    db_password: str
    db_name: str


class DBConnection:

    def __init__(self, db_config: DBConfig):
        pass

    def connect(self):
        pass

    def insert(self, data: BaseModel):
        pass

    def update(self, data: BaseModel):
        pass

    def delete(self, data: BaseModel):
        pass

    def get_by_id(self, id: int):
        pass

    def get_all(self):
        pass

    def query(self, query: str):
        pass

    def disconnect(self):
        pass


class DBOpearation:
    model: type = None
    db_config: dict = None
    db_conn = None

    def __init__(self, model: type, db_config: dict = None, db_conn=None):
        self.model = model
        self.db_config = db_config
        self.db_conn = db_conn

    def db_init(self):
        pass

    def insert(self, data: BaseModel):
        if isinstance(data, self.model):
            db