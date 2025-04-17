from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello mundo"}
@app.get("/teste1")
async def root():
    return {"teste": "deu certo"}