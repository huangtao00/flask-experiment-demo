from flask import Flask , render_template, request
from model import db
import os 
PATH_HERE=os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(PATH_HERE,"test.db")
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY="FUCK"


app=Flask(__name__)
from  view import *   #must use this style of code (import view does not work)

app.config.from_object(__name__)
db.init_app(app)

def main():
	db.create_all()

if __name__=="__main__":
	# with app.app_context():
	# 	main()
	app.run(debug=True,port=8082)

