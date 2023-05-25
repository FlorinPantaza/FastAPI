from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

# CREATE, READ, UPDATE, DELETE
# GET, POST, PUT, DELETE

class Item(BaseModel):
    nume: str
    pret: int 

class UpdateItem(BaseModel):
    nume: str 
    pret: int

cars = {
    1:{
        "nume" : "VW",
        "pret" : 5000
    },
    2:{
        "nume" : "Dacia",
        "pret" : 1000,
    },
}


@app.get('/')
def acasa():
    return{"Mesaj": "Salutare lume !"}

@app.get('/contact')   
def contact():
    return {"Contact" : "Aceasta este pagina de contact"} 

@app.get('/get_car/{item_id}')
def get_car (item_id: int): 
    return cars[item_id] 

@app.post('/create_car/{item_id}')
def create_car(item_id: int, item: Item): 
    if item_id in cars:
        return {" Eroare":"Acest ID deja exista!"}
    cars[item_id] = {"nume": item.nume, "pret": item.pret}
    return cars[item_id] 

@app.delete('/delete_car/')
def delete_car(item_id: int):
    if item_id not in cars:
        return {'Eroare':'Acest ID nu exista !!!'}
    del cars[item_id] 
    return {'WELL DONE': 'ID-ul selectat de tine a fost sters cu succes'}  

@app.put('/update_cars/{item_id}') 
def update_cars(item_id: int, item: UpdateItem):
    if item_id not in cars:
        return HTTPException(status_code=404,detail="Acest ID nu exista in lista noastra")
    if item.nume != None:
        cars[item_id]["nume"] = item.nume
    if item.pret != None:
        cars[item_id]["pret"] = item.pret
    return cars[item_id]              







