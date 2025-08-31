import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.engine import Base


class DBBlogType(Base):
    __tablename__ = "blog_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)


class DBBlog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=False)
    data = Column(DateTime, default=datetime.datetime.now)
    blog_type_id = Column(Integer, ForeignKey("blog_type.id"))

    blog_type = relationship(DBBlogType)

