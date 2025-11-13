import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ciphers.caesar import encrypt_caesar, decrypt_caesar
from ciphers.rail_fence import fence_encrypt, fence_decrypt


class CipherCaesar(BaseModel):
    text: str
    offset: int
    mode: str


class CipherFence(BaseModel):
    text: str


app = FastAPI()


@app.get("/test")
def test():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def test(name):
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar(body: CipherCaesar):
    offset = body.offset
    if body.mode == "encrypt":
        encrypt = encrypt_caesar(body.text, offset)
        return {"encript_text": f"{encrypt} "}

    elif body.mode == "decrypt":
        decrypt = decrypt_caesar(body.text, offset)
        return {"encript_text": f"{decrypt} "}

    raise HTTPException(status_code=404, detail="not found")


@app.get("/fence/encrypt")
def encrypt_fence(txt):
    return {"encrypt_text": f"{fence_encrypt(txt)}"}


@app.post("/fence/decrypt")
def decrypt_fence(txt: CipherFence):
    return {"decrypt_text": f"{fence_decrypt(txt.text)}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
