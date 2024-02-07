"""
This file implements the KITA API with fast api


author: Leon Wempe


"""


import os
import sys


import pickle

import traceback


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


class Manga(BaseModel):
   
    """
    Diese Klasse definiert den Übergabetyp
    für die Artikelnummern
    """
   
    Title: str
    NumberPages: int
    MinutesSketch: int
    MinutesInk: int
    MinutesRaster: int
    CardsSketch: int
    CardsInk: int
    CardsRaster: int
    Cards: list
    WeekDays: list[int]
    StartTime: str
    EndTime: str



app = FastAPI()


origins = ["*"]

app.add_middleware(  
CORSMiddleware,   
allow_origins=origins,  
allow_credentials=True,   
allow_methods=["*"],   
allow_headers=["*"],
)


@app.on_event("shutdown")
def shutdown_event():
    sys.exit(0)



@app.post("/save")
def save_data(manga: Manga):
   
    save_dict = {
                "Title": manga.Title,
                "NumberPages": manga.NumberPages,
                "MinutesSketch": manga.MinutesSketch,
                "MinutesInk": manga.MinutesInk,
                "MinutesRaster": manga.MinutesRaster,
                "CardsSketch": manga.CardsSketch,
                "CardsInk": manga.CardsInk,
                "CardsRaster": manga.CardsRaster,
                "Cards": manga.Cards,
                "WeekDays": manga.WeekDays,
                "StartTime": manga.StartTime,
                "EndTime": manga.EndTime
              }
    with open('save.pickle', 'wb') as handle:
        pickle.dump(save_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    return {
        "message": "success"
    }

@app.post("/load")
def save_data():

    with open('save.pickle', 'rb') as handle:
        save_dict = pickle.load(handle)
   
    return {
        "manga": save_dict
    }