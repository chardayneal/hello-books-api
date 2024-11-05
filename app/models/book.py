from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.author import Author
from app.db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
    author: Mapped[Optional["Author"]] = relationship(back_populates="books")

    @classmethod
    def from_dict(cls, new_dict):
        return Book(title=new_dict["title"] , description=new_dict["description"], author_id=new_dict["author_id"])

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }