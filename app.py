from flask import Flask, render_template, request
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/')
def home():
    return "Flask is working!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # create user object
        new_user = User(name=name, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return "User registered successfully!"

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)