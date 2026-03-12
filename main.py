from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

f = open("quotes.txt" , 'r')
r = f.readlines()
f2 = open("facts.txt" , 'r')
r2 = f2.readlines()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all websites
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/quote")
def get_quote():
    return {"Quote": random.choice(r)}

@app.get("/fact")
def get_fact():
    return {"F-Fact": random.choice(r2)}

