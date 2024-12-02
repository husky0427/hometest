from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root(name: str = None):
    if name:
        return {"message": f"hello, {name}!"}
    return {"message": "Hello, World!"}
