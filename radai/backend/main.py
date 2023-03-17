from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import pig_latin
from pydantic import BaseModel

app = FastAPI()
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Request(BaseModel):
    sentence: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/translate")
async def translate(request: Request):
    return {"translation": pig_latin(request.sentence)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000,reload=True)