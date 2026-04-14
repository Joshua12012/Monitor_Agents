from fastapi import FastAPI, Depends
from auth import verify_token
from database import get_db, engine
from models import Base, Agent, AgentCreate, StatusUpdate
from llm import get_health_summary
from fastapi import Security


from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

Base.metadata.create_all(bind=engine)  # creates tables on startup
app = FastAPI()

@app.post("/agents", dependencies=[Depends(verify_token)])
def register_agent(body: AgentCreate, db=Depends(get_db)):
    agent = Agent(name=body.name, type=body.type)
    db.add(agent); db.commit(); db.refresh(agent)
    return agent

@app.patch("/agents/{agent_id}", dependencies=[Depends(verify_token)])
def update_status(agent_id: str, body: StatusUpdate, db=Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    agent.status = body.status
    agent.status_log += f" -> {body.status}"
    db.commit(); return agent

@app.get("/agents", dependencies=[Depends(verify_token)])
async def list_agents(db=Depends(get_db)):
    agents = db.query(Agent).all()
    result = []
    for a in agents:
        summary = await get_health_summary(a.name, a.status_log)
        result.append({**a.__dict__, "health_summary": summary})
    return result