from fastapi import APIRouter, FastAPI
from pydantic import BaseModel



class CRUDServer:
    model: type = None
    router: APIRouter = None
    endpoint: str = None

    def __init__(self, model: type, router=None):
        self.model = model
        self.endpoint = '/' + model.__name__.lower()

        if router is not None:
            self.router = router




    def _isready(self):
        if self.app is None or self.router is None:
            return False
        return True
    

    def __create(self):
        def _create_inner(body: self.model):
            f"""Creates a new {self.model.__name__} object."""
            return body
        
        return _create_inner
    

    def __list(self):
        def _list_inner():
            f"""Returns a list of {self.model.__name__} objects."""
            return None

        return _list_inner
    

    def __get(self):
        def _get_inner(id: int):
            f"""Returns a {self.model.__name__} object."""
            return None

        return _get_inner

    def __update(self):
        def _update_inner(id: int, body: self.model):
            f"""Updates a {self.model.__name__} object."""
            return None

        return _update_inner
    
    def __delete(self):
        def _delete_inner(id: int):
            f"""Deletes a {self.model.__name__} object."""
            return None

        return _delete_inner


    def initiate(self):
        self.router.post(self.endpoint)(self.__create())
        self.router.get(self.endpoint)(self.__list())
        self.router.get(self.endpoint + '/{id}')(self.__get())
        self.router.put(self.endpoint + '/{id}')(self.__update())
        self.router.delete(self.endpoint + '/{id}')(self.__delete())

