from flask import Flask, jsonify,request


app = Flask(__name__)

books =  [{
    "id": 2, "title": "Flask 101"},
{
    "id": 3, "title": "python for APIs"},
{ "id": 4, "title":"Alchemist"},
{ "id":5, "title": "art of war"}
]

@app.route('/books')

def get_books():
    return jsonify(books)

@app.route('/book/<int:book_id>')
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    return jsonify(book) if book else jsonify({"error": "Book not found"}), 404

@app.route('/books/search')
def search_books():
    title = request.args.get('title')
    
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    results = [b for b in books if title.lower() in b['title'].lower()]
    
    if results:
        return jsonify(results)
    return jsonify({"message": "No books found matching the search criteria"}), 404

if __name__ == '__main__':
    app.run(debug=True)

