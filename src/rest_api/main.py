from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Store the latest mission
mission_data = None

class Mission(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

@app.post("/mission")
def post_mission(mission: Mission):
    global mission_data
    mission_data = mission
    return {"message": "Mission received", "mission": mission}

@app.get("/mission")
def get_mission():
    if mission_data:
        return mission_data
    return {"message": "No mission available"}
