from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', user=None)

if __name__ == "__main__":
    app.run(host="192.168.0.105", port=5555)