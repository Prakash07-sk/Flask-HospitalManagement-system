from flask import Blueprint, render_template,  redirect, url_for, request, session
from validate.validation import Validation
from flask_sqlalchemy import SQLAlchemy
from validate.database import User, db

routes=Blueprint("routes", __name__, static_folder="static", template_folder="templates")




@routes.route('/')

def index():
	return render_template("index.html", title="Hospital Management")

@routes.route('/login',methods=['GET', 'POST'])
def login():
	session.clear()
	if request.method== 'POST':
		session.permanent=True
		username=str(request.form['username']).lower()
		password=str(request.form['password']).lower()
		res=Validation().login(username,password)
		if res=='none':
			return render_template('login.html', error="*username and password does not match")
		else:
			session['username']=username
			return redirect(url_for('routes.management'))
		if "username" in session:
			return redirect(url_for('routes.management'))
	return render_template("login.html", title="Login")
@routes.route('/management')
def management():
	if 'username' in session:
		username = session['username']
		return render_template("management.html", title="Management", values=User.query.all())
	else:
		return redirect(url_for('routes.login'))

@routes.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('routes.login'))

@routes.route('/NewPatients',methods=['GET', 'POST'])
def NewPatients():
	if 'username' in session:
		username = session['username']
		if request.method== 'POST':
			fname=str(request.form['fname']).lower()
			lname=str(request.form['lname']).lower()
			age=str(request.form['age'])
			address=str(request.form['address']).lower()
			country=str(request.form['country']).lower()
			state=str(request.form['state']).lower()
			ssnid=str(request.form['ssnid']).lower()
			bedtype=str(request.form['bedtype']).lower()
			found_user=User.query.filter_by(ssnid=ssnid).first()
			if found_user:
				return render_template("NewPatients.html", ssnid=ssnid,fname=fname,lname=lname,age=age,address=address,title="AddPatient",messages="*ssnid Already exit")
			else:
				upload=User(ssnid=ssnid,fname=fname,lname=lname,age=age,address=address,country=country,state=state,bedtype=bedtype)
				db.session.add(upload)
				db.session.commit()
				return render_template("NewPatients.html", title="AddPatient",message="upload Successful")
		return render_template("NewPatients.html", title="AddPatient",name=username)
	else:
		return redirect(url_for('routes.login'))

@routes.route('/UpdatePatient',methods=['GET', 'POST'])
def UpdatePatient():
	if 'username' in session:
		username = session['username']
		if request.method== 'POST':
			if(request.form.get('action') == "search"):
				ssnid=str(request.form['ssnid']).lower()
				found_user=User.query.filter_by(ssnid=ssnid).first()
				if found_user:
					session['ssnid']=ssnid
					return render_template("UpdateTable.html",ssnid=found_user.ssnid,fname=found_user.fname,lname=found_user.lname,age=found_user.age,doj=found_user.doj,address=found_user.address,state=found_user.state,country=found_user.country,bedtype=found_user.bedtype)

				else:
					return render_template("UpdatePatient.html", title="UpdatePatient",message="*Patient ID does not found ",ssnid=ssnid)
		if request.method== 'POST':
			if(request.form.get('action') == "update"):
				found_user=User.query.filter_by(ssnid=session['ssnid']).first()
				found_user.fname= str(request.form['fname']).lower()
				found_user.lname=str(request.form['lname']).lower()
				found_user.address=str(request.form['address']).lower()
				found_user.age=str(request.form['age']).lower()
				found_user.country=str(request.form['country']).lower()
				found_user.state=str(request.form['state']).lower()
				found_user.bedtype=str(request.form['bedtype']).lower()
				db.session.commit()
				return render_template("UpdatePatient.html",success="Update Successful")

		return render_template("UpdatePatient.html", title="UpdatePatient",name=username)
	else:
		return redirect(url_for('routes.login'))


@routes.route('/DeletePatient',methods=['GET', 'POST'])
def DeletePatient():
	if 'username' in session:
		username = session['username']
		if request.method== 'POST':
			if(request.form.get('action') == "search"):
				ssnid=str(request.form['ssnid']).lower()
				found_user=User.query.filter_by(ssnid=ssnid).first()
				if found_user:
					session['ssnid']=ssnid
					return render_template("DeleteTable.html",ssnid=found_user.ssnid,fname=found_user.fname,lname=found_user.lname,age=found_user.age,doj=found_user.doj,address=found_user.address,state=found_user.state,country=found_user.country,bedtype=found_user.bedtype)

				else:
					return render_template("DeletePatient.html", title="UpdatePatient",message="*Patient ID does not found ",ssnid=ssnid)
		if request.method== 'POST':
			if(request.form.get('action') == "delete"):
				found_user=User.query.filter_by(ssnid=session['ssnid']).first()
				db.session.delete(found_user)
				db.session.commit()
				return render_template("UpdatePatient.html",success="Deleted Patient detail from database")
		return render_template("DeletePatient.html")
	else:
		return redirect(url_for('routes.login'))

@routes.route('/SearchPatient',methods=['GET', 'POST'])
def SearchPatient():
	if 'username' in session:
		username = session['username']
		if request.method== 'POST':
			ssnid=str(request.form['ssnid']).lower()
			found_user=User.query.filter_by(ssnid=ssnid).first()
			if found_user:
				return render_template("SearchPatient.html",title="search Patient's Details",ssnid=found_user.ssnid,fname=found_user.fname,lname=found_user.lname,age=found_user.age,doj=found_user.doj,address=found_user.address,state=found_user.state,country=found_user.country,bedtype=found_user.bedtype)
			else:
				return render_template("SearchPatient.html",title="search Patient's Details",message="*Patient details not found",ssnid=ssnid)
		return render_template("SearchPatient.html",title="search Patient's Details")
	else:
		return redirect(url_for('routes.login'))
