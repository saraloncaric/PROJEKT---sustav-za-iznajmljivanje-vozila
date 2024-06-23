from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db, init_db_command, init_app
from reservation import bp as reservation_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(reservation_bp)

init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
