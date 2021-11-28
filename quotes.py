from flask import Flask ,render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:M@y08352@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://ixiahucmwiszeu:8b7ab2b527e9d0712bbff4099309a7a347a1b7b7947bcd743f311b5ffaf49bf7@ec2-54-175-147-69.compute-1.amazonaws.com:5432/d62srch39nc2gf'
app.config['SQLALCHEMY_TRAC_MODIFIATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes(): 
	return render_template('quotes.html')

@app.route('/process',methods = ['Post'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata = Favquotes(author=author, quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))
 