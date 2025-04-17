from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello mundo"}
@app.get("/teste1")
async def root():
    return {"teste": True, "num_aleatorio": random.randint(0, 10000)}