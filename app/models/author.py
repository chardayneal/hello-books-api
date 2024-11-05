from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.book import Book

class Author(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, author_data):
        return cls(name=author_data["name"]) 
    
    