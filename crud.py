from sqlalchemy.orm import Session

from db.models import DBBlogType
from schemas import BlogTypeCreate

def get_all_blog_types(db: Session):
    return db.query(DBBlogType).all()

def create_blog_type(db: Session, blog_type: BlogTypeCreate):
    db_blog_type = DBBlogType(
        name=blog_type.name,
    )
    db.add(db_blog_type)
    db.commit()
    db.refresh(db_blog_type)

    return db_blog_type