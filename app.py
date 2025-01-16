from flask import Flask
from flask import render_template

app = Flask(__name__)

# index route for web app
@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9874)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_there(name_data=None):
    return render_template('hello_there.html', name=name_data)