from fastapi import FastAPI

# para levantar el servidor de prueba
# uvicorn main:app --reload

app = FastAPI()


@app.get('/')
# la operación que ejecutamos es asíncrona
async def root():
    return "Hola FastAPI!!"


@app.get('/url_curso')
async def url_prueba():
    return {"url_prueba": "https://google.com"}
