from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.model.book import Book
from app.model.author import Author


session = SessionLocal()
app = FastAPI()


class sBook(BaseModel):
    title: str
    description: str
    # author: str
    id: int
    author_id: int


class sAuthor(BaseModel):
    name: str
    firstname: str
    country: str
    id: int



@app.get("/")
def read_root():
    return {"name": "Terminus library",
            "description": "api backend to create book, and manage loan of the books"}


@app.get("/books/")
def read_books():
    print("Start reading all books")
    res = session.query(Book)
    return {"books": res.all()}

#Exemple d'appel GET /books/:
# curl http://localhost:88/books/



@app.post("/book/")
def create_book(book: sBook):
    print("ADD BOOK START")
    print(book.dict())
    # {'title': 'fondation', 'description': 'livre de SF', 'author': 'Isaac Asimov', 'id': 2}
    newbook = Book()
    newbook.id = book.id # gerer un auto increment en bdd
    newbook.title = book.title
    newbook.description = book.description
    # newbook.author = book.author
    newbook.author_id = book.author_id
    res = session.add(newbook)
    session.commit()
    session.refresh(newbook)
    return {"id": newbook.id}

# Exemple d'appel POST /book/:
# curl -d \
#   '{"id": 1,
#     "title":"fondation",
#     "description": "livre de SF",
#     "author_id": 1,
#     "author": "Isaac Asimov"}' \
#   -H "Content-Type: application/json" -X \
#   POST http://localhost:88/book/


@app.post("/author/")
def create_author(author: sAuthor):
    print("ADD author START")
    print(author.dict())
    newauthor = Author()
    newauthor.id = author.id  # TODO: gerer un auto increment en bdd
    newauthor.name = author.name
    newauthor.firstname = author.firstname
    newauthor.country = author.country

    res = session.add(newauthor)

    session.commit()
    session.refresh(newauthor)
    return {"id": newauthor.id}

# Exemple d'appel POST /author/:
# curl -d \
#   '{"id": 1, 
#     "name":"Asimov", 
#     "firstname": "Isaac", 
#     "country": "US"}' \
#   -H "Content-Type: application/json" -X \
#   POST http://localhost:88/author/