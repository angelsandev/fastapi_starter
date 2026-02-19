from fastapi import FastAPI

app = FastAPI()

app.title = "Proyecto EAN | Python FastAPI"
app.version = "0.1.0"

@app.get("/")
def read_root():
    return {"Hello": "YO"}

@app.get("/", tags=["Home"])
def home():
    return {"Menú Home"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}