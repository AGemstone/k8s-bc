from datetime import datetime
from os import environ

from fastapi import FastAPI, Request, Depends

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

db_user = environ["DB_USER"]
db_pass = environ["DB_PASS"]
db_name = environ["DB_NAME"]
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True)
    visited_at = Column(DateTime)
    ip = Column(String(40))

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/log")
async def log(request: Request, db: Session = Depends(get_db)):
    log_entry = Log(ip=request.client.host, visited_at=datetime.now())
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)

    return {"message": "ok!"}
