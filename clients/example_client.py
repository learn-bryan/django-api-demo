import requests

def create_book(title, author, isbn):
    headers = {
        'title': title,
        'author': author,
        'isbn': isbn
    }

    response = requests.post('https://localhost:8000/books/', headers)
    print(f"New book {title} by {author} with ISBN: {isbn} has been created.\n\n")

def get_all_books():
    response = requests.get('http://localhost:8000/books/')
    return response.json()

books = get_all_books()
for book in books:
    print(f"Book {book['id']}:")
    print(f"    Title: {book['title']}")
    print(f"    Author: {book['author']}")
    print(f"    ISBN: {book['isbn']}")

