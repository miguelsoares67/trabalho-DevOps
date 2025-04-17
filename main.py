from fastapi import FastAPI
app = FastAPI()
@app.get("/helloworld")
async def root():
    return {"message": "Hello mundo"}
@app.get("/funcaoteste")
async def root():
    return {"teste": "deu certo"}