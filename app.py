from flask import Flask, render_template, request, redirect, url_for
import openpyxl

app = Flask(__name__)
EXCEL_FILE = 'Library.xlsx'

def load_books():
    wb = openpyxl.load_workbook(EXCEL_FILE)
    sheet = wb.active
    books = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        books.append({
            'Book ID': row[0],
            'Title': row[1],
            'Author': row[2],
            'Status': row[3]
        })
    return books

def save_books(books):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Book ID', 'Title', 'Author', 'Status'])
    for book in books:
        ws.append([book['Book ID'], book['Title'], book['Author'], book['Status']])
    wb.save(EXCEL_FILE)

@app.route('/')
def home():
    books = load_books()
    available = sum(1 for b in books if b['Status'] == 'Available')
    issued = sum(1 for b in books if b['Status'] == 'Issued')
    return render_template('home.html', available=available, issued=issued)

@app.route('/books')
def book_list():
    books = load_books()
    return render_template('books.html', books=books)

@app.route('/issue', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        books = load_books()
        for book in books:
            if book['Book ID'] == book_id and book['Status'] == 'Available':
                book['Status'] = 'Issued'
                save_books(books)
                return redirect(url_for('book_list'))
        return "Book not available or already issued."
    return render_template('issue.html')

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        books = load_books()
        for book in books:
            if book['Book ID'] == book_id and book['Status'] == 'Issued':
                book['Status'] = 'Available'
                save_books(books)
                return redirect(url_for('book_list'))
        return "Book not found or already returned."
    return render_template('return.html')

if __name__ == '__main__':
    app.run(debug=True)