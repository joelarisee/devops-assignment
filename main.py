import os
from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(String)

Base.metadata.create_all(bind=engine)
app = FastAPI()

def verify_header(authorization: str = Header(None)):
    if authorization != "pay3-assignment":
        raise HTTPException(status_code=401, detail="Unauthorized")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", dependencies=[Depends(verify_header)])
def create_item(name: str, value: str, db: Session = Depends(get_db)):
    db_item = Item(name=name, value=value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Entry created", "item": db_item}

@app.get("/items/", dependencies=[Depends(verify_header)])
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()