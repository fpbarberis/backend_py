from fastapi import FastAPI
from pydantic import BaseModel

# para levantar el servidor de prueba
# uvicorn users:app --reload

# url documentacion FASTAPI
# localhost + /docs

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Jhon", surname="Doe", url="www.paginajhon.com", age=30),
              User(id=2, name="Jane", surname="Doe", url="www.paginaJane.com", age=31)]


@app.get('/usersjson')
# la operación que ejecutamos es asíncrona
async def usersjson():
    return users_list


@app.get('/users/{id}')
# la operación que ejecutamos es asíncrona
async def user(id: int):
    # filtramos la lista de usuarios por id
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No existe usuario asociado a ese ID"}


@app.get('/userquery/')
# localhots + /userquery/?id=1 para buscar por id en la query GET
# la operación que ejecutamos es asíncrona
async def user(id: int):
    # filtramos la lista de usuarios por id
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No existe usuario asociado a ese ID"}
