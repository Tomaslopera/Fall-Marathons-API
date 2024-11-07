from fastapi import APIRouter, HTTPException, Depends, Query
from config.db_connection import conn, session
from schemas.models import Marathon
from sqlalchemy import select, text
from typing import List
import json

marathon = APIRouter()

with open("marathons.json", "r") as file:
    marathon_data = json.load(file)["marathons"]
    

@marathon.get("/marathons/{race}", tags=["marathons"], description="Get the results of a single marathon")
def get_marathon(race: str, offset: int = 0, limit: int = Query(100, le=100)):
    
    marathons = [entry for entry in marathon_data if entry["Race"].lower() == race.lower()]
    
    limited_marathons = marathons[offset: offset + limit]

    if not limited_marathons:
        raise HTTPException(status_code=404, detail="Marathon not found")

    return {
        "marathons": limited_marathons,
        "next_offset": offset + limit if len(limited_marathons) == limit else None
    }

@marathon.post("/add_marathon", tags=["marathons"], description="Add a new result for a Marathon")
def add_marathon_result(m: Marathon):
    new_entry = m.dict()
    marathon_data.append(new_entry) 

    try:
        with open("marathons.json", "w") as file:
            json.dump({"marathons": marathon_data}, file, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving the marathon data to file")

    return {
        "new_marathon": new_entry,
        "total_records": len(marathon_data)
    }