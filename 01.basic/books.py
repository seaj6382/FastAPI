from fastapi import FastAPI, APIRouter

# 로컬 메로리 DB - 서버를 종료하면 데이터가 사라짐.
BOOKS = [
    {
        'id':1,
        'title': '사라진 물고기',
        'author': '아무개',
        'url': 'https://www.yes24.com/사라진물고기'
    }
]

app = FastAPI()
router = APIRouter()

# 루트 페이지
@router.get('/', status_code=200)
def main() -> dict:
    return {'Message':'Welcome to the book World!'} # 템플릿 코드

# 전체 팩 데이터 조회
@router.get('/api/v1/books', status_code=200)
def get_all_books() -> list:
    return BOOKS #[{book1}, {book2}]

# 특정 책 데이터 조회
@router.get('/api/v1/books/{book_id}')
def get_book(book_id: int):
    # pass
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    if book:
        return book
    return {'error': f'Book not found, ID: {book_id}'}

    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         book
    #         break

# 책 생성
@router.post('/api/v1/books/')
def create_book(book: dict):
    # {'id':2, 'title': ''...}
    BOOKS.append(book)
    return book

# 책 수정
@router.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book_update: dict):
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    for key, value in book_update.items():
        if key in book:
            book[key] = value
    
    return book

# 책 삭제
@router.delete('/api/v1/books/{book_id}')
def delete_book(book_id: int):
    global BOOKS
    BOOKS = [item for item in BOOKS if item['id'] != book_id]

    return {'message':'Successfully dleted book, ID: {book_id}'}

    # for item in BOOKS:
    #     if item['id'] != book_id:
    #         item

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('books:app', port=8001, reload=True)