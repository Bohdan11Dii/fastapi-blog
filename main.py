
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from db.engine import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}


@app.get("/blog_types/", response_model=list[schemas.BlogType])
def read_blog_types(db: Session = Depends(get_db)):
    return crud.get_all_blog_types(db=db)


@app.post("/blog_types/", response_model=schemas.BlogType)
def create_blog_types(
        blog_type: schemas.BlogTypeCreate,
        db: Session = Depends(get_db)
):
    db_blog_type = crud.get_blog_type_by_name(db=db, name=blog_type.name)
    if db_blog_type:
        raise HTTPException(
            status_code=400,
            detail="Blog type already exists"
        )

    return crud.create_blog_type(db=db, blog_type=blog_type)
