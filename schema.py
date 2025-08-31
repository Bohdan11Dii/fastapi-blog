from pydantic import BaseModel

class BlogTypeBase(BaseModel):
    name: str


class BlogTypeCreate(BlogTypeBase):
    ...


class BlogType(BlogTypeBase):
    id: int

    class Config:
        orm_mode = True