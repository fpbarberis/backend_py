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


def search_user(id: int):
    # filtramos la lista de usuarios por id
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No existe usuario asociado a ese ID"}


users_list = [User(id=1, name="Jhon", surname="Doe", url="www.paginajhon.com", age=30),
              User(id=2, name="Jane", surname="Doe", url="www.paginaJane.com", age=31)]


@app.get('/usersjson')
# la operación que ejecutamos es asíncrona
async def usersjson():
    return users_list


@app.get('/users/{id}')
# la operación que ejecutamos es asíncrona
async def user(id: int):
    return search_user(id)


@app.get('/userquery/')
# localhots + /userquery/?id=1 para buscar por id en la query GET
# la operación que ejecutamos es asíncrona
async def user_query(id: int):
    return search_user(id)


@app.post('/users/')
# utilizamos nuestra calse User
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        # agrega a nuestra lista de usuarios, un nuevo usuario. en el PUT deben ir los datos como JSON
        users_list.append(user)


@app.put('/users/')
async def user(user: User):

    found = False

    # buscamos el usuario en nuestros datos
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
