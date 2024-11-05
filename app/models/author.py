from sqlalchemy.orm import Mapped, mapped_column
from app.db import db

class Author(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, author_data):
        return cls(name=author_data["name"]) 
    
    