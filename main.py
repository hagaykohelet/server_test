import json

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uvicorn
from ciphers.caesar import encript_caesar, decript_caesar


class Cipher(BaseModel):
    text: str
    offset: int
    mode: str


app = FastAPI()


# def read_json(file):
#     with open (file, "r") as f:
#         json.load(f)

@app.get("/test")
def test():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def test(name):
    return {"msg": f"user :{name}"}


@app.post("/caesar")
def encript(body: Cipher):
    offset = body.offset
    if body.mode == "encript":
        return encript_caesar(body.text, offset)
    elif body.mode == "decript":
        return decript_caesar(body.text, offset)

    raise HTTPException(status_code=404, detail= "not found")




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
