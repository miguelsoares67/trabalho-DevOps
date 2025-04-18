from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/helloworld")
async def root():
    return {"message": "Hello mundo"}

@app.get("/funcaoteste")
async def root():
    return {"teste": True, "num_aleatorio": random.randint(0, 10000)}