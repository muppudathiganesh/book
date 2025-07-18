from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary of sample recommended books by genre
book_data = {
    "fiction": [
        "The Great Gatsby", 
        "To Kill a Mockingbird", 
        "1984"
    ],
    "mystery": [
        "Gone Girl", 
        "The Girl with the Dragon Tattoo", 
        "Sherlock Holmes"
    ],
    "fantasy": [
        "Harry Potter", 
        "The Hobbit", 
        "Percy Jackson & the Olympians"
    ],
    "science": [
        "A Brief History of Time", 
        "Sapiens", 
        "The Selfish Gene"
    ],
    "romance": [
        "Pride and Prejudice", 
        "Me Before You", 
        "The Notebook"
    ]
}

# Home route with genre form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        genre = request.form.get('genre', '').strip().lower()
        return redirect(url_for('recommendations', genre=genre))
    return render_template('genre_form.html')

# Dynamic route to show book recommendations
@app.route('/books/<genre>')
def recommendations(genre):
    books = book_data.get(genre, [])
    return render_template('books.html', genre=genre.title(), books=books)

if __name__ == '__main__':
    app.run(debug=True)
