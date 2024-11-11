from flask import Flask,render_template,request 
from backend import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/profile', methods = ['POST', "GET"])
def user():
    output = request.form.to_dict()
    name = output["name"]
    if name == "no":
        name = create_random_user()
    return render_template('user.html', name=name)


@app.route("/fruit", methods=['GET', 'POST'])
def get_fruit():
    output = request.form.to_dict()
    fruit_name = output["fruit"]
    fruit_data = generate_fruit_data(fruit_name)
    return render_template('fruit.html', fruit = fruit_data, fruit_name = fruit_name)

@app.route('/birthday_fact', methods=['GET', 'POST'])
def get_birthday():
    output = request.form
    date = output["date"]
    date_fact = birthday_fact(date)
    return render_template('birthday.html', date_fact=date_fact, date = date)

@app.route('/HP_char', methods=['GET', 'POST'])
def get_char_hp():
    output = request.form
    char = output['char']
    index_char = int(char)
    char_fact, image = get_harry_potter_char_facts(index_char)
    return render_template("hp_char.html", char_fact = char_fact, char_image=image)

@app.route('/hp_books', methods=['GET', 'POST'])
def get_books_hp():
    output = request.form
    books = output['books']
    index_books = int(books)
    book_fact, book_image = get_harry_potter_facts(index_books)
    return render_template('hp_books.html', book_fact=book_fact, book_image=book_image)

if __name__ == "__main__":
    app.run(debug=True)