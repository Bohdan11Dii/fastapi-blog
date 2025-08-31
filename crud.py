from sqlalchemy.orm import Session

from db import models
from schemas import BlogTypeCreate

def get_all_blog_types(db: Session):
    return db.query(models.DBBlogType).all()

def get_blog_type_by_name(db: Session, name: str):
    return (
        db.query(models.DBBlogType).filter(models.DBBlogType.name == name).first()
    )

def create_blog_type(db: Session, blog_type: BlogTypeCreate):
    db_blog_type = models.DBBlogType(
        name=blog_type.name,
    )
    db.add(db_blog_type)
    db.commit()
    db.refresh(db_blog_type)

    return db_blog_type