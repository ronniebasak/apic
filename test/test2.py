from apic.server import CRUDServer
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter


class Shona(BaseModel):
    name: str
    age: int
    address: str
    is_employed: bool
    height: float
    hobbies: list = []


app = FastAPI()
server = CRUDServer(
    Shona,
    router=APIRouter(prefix="/test", tags=["test"])
)

if __name__ == "__main__":
    server.initiate()
    app.include_router(server.router)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)