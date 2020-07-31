from flask import Flask,render_template, redirect, url_for
from datetime import timedelta,datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hpmanagement.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app) 

class User(db.Model):
	ssnid=db.Column(db.String(90),primary_key=True)
	fname=db.Column(db.String(100))
	lname=db.Column(db.String(100))
	age=db.Column(db.String(3))  
	doj=db.Column(db.DateTime,default=datetime.now)
	address=db.Column(db.String(100))
	country=db.Column(db.String(100))
	state=db.Column(db.String(100))
	bedtype=db.Column(db.String(100))

	# def __init__(ssnid,fname,lname,age,doj,address,country,state,bedtype):
	# 	self.ssnid=ssnid
	# 	self.fname=fname
	# 	self.lname=lname
	# 	self.age=age
	# 	self.doj=doj
	# 	self.address=address
	# 	self.country=country
	# 	self.state=state
	# 	self.bedtype=bedtype
