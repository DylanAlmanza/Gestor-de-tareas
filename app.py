from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')

@app.route('/add')
def add_task():
    return render_template('add_task.html')


@app.route('/update')
def update_task():
    return render_template('update_task.html')


if __name__ == '__main__':
    app.run(debug=True)