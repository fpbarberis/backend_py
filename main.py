from fastapi import FastAPI

# para levantar el servidor de prueba
# uvicorn main:app --reload

# url documentacion FASTAPI
# localhost + /docs

app = FastAPI()


@app.get('/')
# la operación que ejecutamos es asíncrona
async def root():
    return "Hola FastAPI!!"


@app.get('/url_prueba')
async def url_prueba():
    return {"url_prueba": "https://google.com"}
