from flask import Flask
from flask import render_template

app = Flask(__name__)

# index route for web app
@app.route('/')
def index():
    return render_template('index.html')

 # new functions
@app.route('/about/')
def about():
    # declare variable 
     current_mood = "mid"
     friends_list = ['Eliza', 'Courtney', 'Lucian', 'Alex', 'Abby', 'Sohan', 'Grace']
     definitions = {'platypus':'a blue-green creature that is very good at solving mysteries', 'ladybug':'an apex predator with magical properties','giraffe':'long neck animal with purple tounge'}
     
     # pass variable into rendered template
     return render_template("about.html", mood = current_mood, friends = friends_list, my_dict=definitions)
 

@app.route('/contact/')
def contact():
     return render_template("contact.html")

@app.route('/hello/')
@app.route('/hello/<name_data>')
def hello_there(name_data=None):
    return render_template('hello_there.html', name=name_data)

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

# allows u to click run button
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5421)
    