from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Serve login/registration page"""
    return render_template('index.html')

@app.route('/apps')
def apps():
    """Serve app dashboard page"""
    return render_template('apps.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
