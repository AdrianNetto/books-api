from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    'id': 1,
    'name': 'Dogma e Ritual da Alta Magia',
    'author': 'Eliphas Levi'
  },
  {
    'id': 2,
    'name': 'O Livro da Lei',
    'author': 'Aleister Crowley'
  },
  {
    'id': 3,
    'name': 'Medicina Alquimica',
    'author': 'Paracelso'
  }
]

@app.route('/books', methods=['GET'])
def get_all_books():
  return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)

@app.route('/books/<int:id>', methods = ['PUT'])
def edit_book(id):
  edited_book = request.get_json()
  for index,book in enumerate(books):
    if book.get('id') == id:
      books[index].update(edited_book)
      return jsonify(books[index])
     
@app.route('/books/create', methods = ['POST'])
def create_book():
  new_book = request.get_json()

  books.append(new_book)

  return jsonify(new_book)

@app.route('/books/delete/<int:id>', methods = ['DELETE'])
def delete_book(id):
  for index, book in enumerate(books):
    if book.get('id') == id:
      del books[index]

  return jsonify(books)

app.run(port=5000, host='localhost', debug=True)