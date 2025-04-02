import random
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return FileResponse("test.html")

@app.post("/info")
def info(number : int = Body(embed=True, ge=1, le=6)):
    rand_number = random.randint(1, 6)
    if number == rand_number:
        return {"message": f"Вы угадали. Было загадано число {rand_number}"}
    else:
        return {"message": f"Вы не угадали. Ваше число {number}, а загадано число {rand_number}"}