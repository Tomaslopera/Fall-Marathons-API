from typing import Optional
from pydantic import BaseModel

class Marathon(BaseModel):
    Race: Optional[str] = None
    Year: Optional[int] = None
    Name: Optional[str] = None
    Gender: Optional[str] = None
    Age:  Optional[int] = None
    Finish: Optional[int] = None
    Age_Bracket: Optional[str] = None