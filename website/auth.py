from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from .import db
from .models import User,student,staff, takes, admin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user,login_manager
from datetime import datetime
from flask_login import LoginManager
from flask import Flask
from flask_session import Session
auth=Blueprint('auth',__name__)
@auth.route('/add-student',methods=['GET','POST'])
def add_student():
    if request.method=='POST':
        
        FName= request.form.get('FName')
        uid=request.form.get('uid')
        dob=request.form.get('dob')
        year = int(dob[:4])
        month = int(dob[5:7])
        day = int(dob[8:10])
        branch=request.form['gridRadios']
        email=request.form.get('email')
        father=request.form.get('father')
        mother=request.form.get('mother')
        user=student.query.filter_by(college_email=email).first()
        if user:
            flash('Email already exists',category='error')
        else:
            new_student=student(UID=uid,Full_Name=FName,Mothers_Name=mother,Fathers_Name=father,Phone_No=12345,Address="abcdefg hij",DOB=datetime(year, month, day),Age=18,Fees=10000,Fees_Status="Paid",Attendance=87.3,CGPA=7,Year_of_Graduation=2025,Branch=branch,college_email=email,college_password="abc123")
            db.session.add(new_student)
            if request.form.get('cs103'):
                tk=takes(UID=uid,Course_Code="CS103")
                db.session.add(tk)
            if request.form.get('cs107'):
                tk=takes(UID=uid,Course_Code="CS107")
                db.session.add(tk)
            if request.form.get('cs203'):
                tk=takes(UID=uid,Course_Code="CS203")
                db.session.add(tk)
            
            db.session.commit()
            flash('Account Created',category='success')
            user=student.query.filter_by(college_email=email).first()
            return render_template("admin_profile.html", user=current_user)
    return render_template("add_student.html",user=current_user)

@auth.route('/add-staff',methods=['GET','POST'])
def add_staff():
    if request.method=='POST':
        FName= request.form.get('FName')
        tc=request.form.get('tc')
        dob=request.form.get('dob')
        year = int(dob[:4])
        month = int(dob[5:7])
        day = int(dob[8:10])
        branch=request.form['gridRadios']
        course = request.form.get('course')
        email=request.form.get('email')
        father=request.form.get('father')
        mother=request.form.get('mother')
        user=staff.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category='error')
        else:
            new_staff=staff(Teacher_Code=tc,Full_Name=FName,Mothers_Name=mother,Fathers_Name=father,Phone_Number=12345,Address="abcdefg hij",DOB=datetime(year, month, day),Salary=40000,Attendance=87.3,Qualification = "MTech", Experience = 7,Dept_Name=branch,email=email,teacher_password="abc123",Course_Code=course)
            db.session.add(new_staff)
            db.session.commit()
            flash('Account Created',category='success')
            user=staff.query.filter_by(email=email).first()
            #thrlg(user)
            return render_template("view_staff.html", user=current_user, staff=staff.query.all())
        
    return render_template("add_teacher.html",user=current_user)

@auth.route('/admin-login',methods=['GET','POST'])
def Admin_Login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=admin.query.filter_by(admin_email=email).first()
        if user:
            if (user.admin_password==password):#do hashing here
                session['key']="admin"
                login_user(user,remember=True)
                return redirect(url_for('views.admin_profile'))
            else:
                print("Wrong password")

        else:
            print("NOT WORKING MAN")
    return render_template("Admin_Login.html",user=current_user)

@auth.route('/student-login',methods=['GET','POST'])
def Login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=student.query.filter_by(college_email=email).first()
        if user:
            if (user.college_password==password):#do hashing here
                session['key']="student"
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
            if (user.teacher_password==password):
                session['key']="staff"
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

@auth.route('/teacher-logout')
@login_required
def teacher_logout():
    logout_user()
    return redirect(url_for('auth.Login_Teacher'))

@auth.route('/admin-logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('auth.Admin_Login'))