from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
from datetime import datetime
# initialise the database
db = SQLAlchemy(app)

#create a model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

#create a fuction to return a string when we add 
    def __repr__(self):
        return '<Name %r>' % self.id

clients = []
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form', methods=['POST'])
def form():
    return render_template('form.html')

    if not name or not email or not message:
        error_statement = 'Please, all the filds required.'


if __name__ == '__main__':
    app.run(debug=True)