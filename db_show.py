from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    conn = sqlite3.connect('./phone_price.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phones')
    phones = cursor.fetchall()
    conn.close()
    return render_template('index.html', phones=phones)

if __name__ == "__main__":
    app.run(host='192.168.1.37',port='8594')
