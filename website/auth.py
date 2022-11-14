from flask import Blueprint,render_template,request,flash,redirect,url_for
from .import db
from .models import User,student,staff
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)

@auth.route('/student-login',methods=['GET','POST'])
def Login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=student.query.filter_by(college_email=email).first()
        if user:
            if (user.college_password==password):#do hashing here
                login_user(user,remember=True)
                return redirect(url_for('views.student_profile'))
            else:
                print("Wrong password")

        else:
            print("NOT WORKING MAN")
    return render_template("Login.html",user=current_user)

@auth.route('/teacher-login',methods=['GET','POST'])
def Login_Teacher():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=staff.query.filter_by(email=email).first()
        if user:
            if (user.teacher_password==password):#do hashing here
                login_user(user,remember=True)
                return redirect(url_for('views.teacher_profile'))

        else:
            print("NOT WORKING MAN")
    return render_template("Login_Teacher.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.Login'))