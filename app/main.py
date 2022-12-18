from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.model.book import Book


session = SessionLocal()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


class sBook(BaseModel):
    title: str
    description: str
    author: str
    id: int

# Exemple d'appel:
# curl -d '{"id": 2,
#  "title":"fondation",
#  "description": "livre de SF",
#  "author": "Isaac Asimov"}' -H "Content-Type: application/json" -X POST http://localhost:80/book/

@app.post("/book/")
def create_book(book: sBook):
    print("ADD BOOK START")
    print(book)
    print(*book)
    newbook = Book()
    newbook.id = book.id # gerer un auto increment en bdd
    newbook.title = book.title
    newbook.description = book.description
    
    # book = Book(1, 'titre', 'desc')
    res = session.add(newbook)
    session.commit()
    session.refresh(newbook)
    return {"oh": "yeah", "id": res}
