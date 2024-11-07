from fastapi import APIRouter, HTTPException, Depends, Query
from config.db_connection import conn, session
from schemas.models import Marathon
from sqlalchemy import select, text
from typing import List
import os
import json

marathon = APIRouter()

@marathon.get("/marathons/{race}", tags=["marathons"], description="Get the results of a single marathon",
)
def get_marathon(race: str, offset: int = 0, limit: int = Query(100, le=100)):
    try:
        consulta = text("SELECT * FROM marathonsdata WHERE marathonsdata.Race = :race LIMIT :limit OFFSET :offset") 
        # Aquí se modifican datos en caso de que se quiera extraer algo en específico
        # ejemplo = text("SELECT Race, Year, Name FROM marathonsdata WHERE marathonsdata.Race = :race LIMIT :limit OFFSET :offset")
        result = session.execute(consulta, {"race": race, "limit": limit, "offset": offset})
        
        rows = result.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="Marathon not found")

        marathons = [dict(row._mapping) for row in rows]

        return {
            "marathons": marathons,
            "next_offset": offset + limit if len(marathons) == limit else None
        }
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        return None
    finally:
        session.close()
        

@marathon.post("/add_marathon", tags=["marathons"], description="Add a new result for a Marathon")
def add_marathon_result(m: Marathon):
    try:
        count_before = session.execute(text("SELECT COUNT(*) FROM marathonsdata")).scalar()

        # Inserta el nuevo resultado en la base de datos
        consulta = text("INSERT INTO marathonsdata VALUES (:Race, :Year, :Name, :Gender, :Age, :Finish, :Age_Bracket)")
        valores = {
            "Race": m.Race,
            "Year": m.Year,
            "Name": m.Name,
            "Gender": m.Gender,
            "Age": m.Age,
            "Finish": m.Finish,
            "Age_Bracket": m.Age_Bracket
        }
        session.execute(consulta, valores)
        session.commit()

        count_after = session.execute(text("SELECT COUNT(*) FROM marathonsdata")).scalar()

        consulta = text(
            "SELECT * FROM marathonsdata WHERE Race = :Race AND Name = :Name AND Year = :Year ORDER BY Year DESC LIMIT 1"
        )
        nuevo_maraton = session.execute(consulta, {"Race": m.Race, "Name": m.Name, "Year": m.Year}).first()

        if not nuevo_maraton:
            raise HTTPException(status_code=404, detail="Marathon not found")

        # Se crea una carpeta si no existe para almacenar el archivo
        if not os.path.exists("marathons"):
            os.makedirs("marathons")

        json_data = dict(nuevo_maraton._mapping)
        json_data["uploaded_at"] = datetime.now().isoformat() 

        file_name = f"marathons/{m.Race}_{m.Year}_{m.Name}.json"
        
        # Guarda el JSON en el archivo local
        with open(file_name, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        return {
            "new_marathon": json_data,
            "added_records": count_after - count_before,
            "total_records": count_after
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al insertar en la base de datos: {e}")
        return {"error": "Database insertion error"}, 500
    except Exception as e:
        print(f"Error al guardar JSON: {e}")
        return {"error": "Error generating JSON file"}, 500
    finally:
        session.close()
