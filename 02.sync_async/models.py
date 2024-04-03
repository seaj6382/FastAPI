from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class SearchBook(BaseModel): # Detail - GET
    results: Optional[Book] # Book

from typing import List
class SearchBooks(BaseModel): # BookList - GET
    results: List[Book] # [Book, Bookb, Book, ...]
 