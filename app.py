from flask import Flask, request, render_template, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display():
    df = pd.read_excel('Library.xlsx')
    blogs = df.to_dict('records')
    return render_template('display.html', blogs=blogs)

@app.route('/search')
def search_book():
    title = request.args.get('title', '').strip().lower()
    df = pd.read_excel('Library.xlsx')

    # Normalize title column
    df['title'] = df['title'].astype(str).str.strip().str.lower()

    result_text = "Not Available"
    matching = df[df['title'] == title]

    if not matching.empty:
        status = matching.iloc[0]['status'].strip().lower()
        if status == 'available':
            result_text = "Available"
        elif status == 'issued':
            result_text = " Issued"
        else:
            result_text = f" Status: {status}"

    blogs = df.to_dict('records')
    return render_template('display.html', blogs=blogs, result=result_text)

@app.route('/add')
def add_blog():
    return render_template('add.html')

@app.route('/show')
def show():
    df = pd.read_excel('Library.xlsx')
    blogs = df.to_dict('records')
    return jsonify(blogs)

@app.route('/create', methods=['POST'])
def create_blog():
    title = request.form.get('title')
    author = request.form.get('author')
    status = request.form.get('status')
    df = pd.read_excel('Library.xlsx')
    new_id = df['id'].max() + 1 if not df.empty else 1
    df.loc[len(df)] = [new_id, title, author, status]
    df.to_excel('Library.xlsx', index=False)
    return redirect(url_for('display'))

@app.route('/delete/<string:title>')
def delete(title):
    df = pd.read_excel('Library.xlsxx')
    df = df[df['title'].str.upper().str.strip() != title.upper().strip()]
    df.to_excel('Library.xlsx', index=False)
    return redirect(url_for('display'))

@app.route('/edit/<int:blog_id>')
def edit_blog(blog_id):
    df = pd.read_excel('Library.xlsx')
    blog_row = df[df['id'] == blog_id]
    if blog_row.empty:
        return "Book not found", 404
    blog = blog_row.to_dict('records')[0]
    return render_template('edit.html', blog=blog)

@app.route('/api/update/<int:blog_id>', methods=['PUT'])
def api_update_blog(blog_id):
    df = pd.read_excel('Library.xlsx')
    if blog_id in df['id'].values:
        data = request.get_json()
        df.loc[df['id'] == blog_id, 'title'] = data.get('title')
        df.loc[df['id'] == blog_id, 'author'] = data.get('author')
        df.loc[df['id'] == blog_id, 'status'] = data.get('status')
        df.to_excel('Library.xlsx', index=False)
        return jsonify({"message": "Book updated"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/api/delete/<int:blog_id>', methods=['DELETE'])
def api_delete_blog(blog_id):
    df = pd.read_excel('Library.xlsx')
    if blog_id in df['id'].values:
        df = df[df['id'] != blog_id]
        df.to_excel('Library.xlsx', index=False)
        return jsonify({"message": "Book deleted"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    title = data['title']
    author = data['author']
    status = data['status']
    df = pd.read_excel('Library.xlsx')
    new_id = df['id'].max() + 1 if not df.empty else 1
    df.loc[len(df)] = [new_id, title, author, status]
    df.to_excel('Library.xlsx', index=False)
    return jsonify({'Message': 'Success...Data Inserted'})

if __name__ == '__main__':
    app.run(debug=True)