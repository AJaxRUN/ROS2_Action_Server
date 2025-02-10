from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

missions = []

class Mission(BaseModel):
    mission_id: int

@app.post("/mission")
def post_mission(mission: Mission):
    missions.append(mission.mission_id)
    return {"message": "Mission received", "mission": mission.mission_id}

@app.get("/mission")
def get_mission():
    global missions
    if len(missions):
        return {"mission": missions.pop(0)}
    else: 
        return {"mission": {}}
