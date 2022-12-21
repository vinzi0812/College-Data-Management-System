#from unicodedata import category
from flask import Blueprint,render_template,request,flash,redirect,url_for, jsonify
from flask_login import login_required,current_user
from .models import User,student,staff, takes, admin
from . import db
import json
import sqlite3
views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/delete-staff/<int:Teacher_Code>',methods=['GET','POST'])
@login_required
def delete_staff(Teacher_Code):
    print('IT IS WORKING')
    conn = sqlite3.connect('DBMS1/instance/College.db')
    c = conn.cursor()
    c.execute("DELETE FROM staff WHERE Teacher_Code = ?",(Teacher_Code))
    conn.commit()
    conn.close()
    return render_template("delete.html",user=current_user, staff=staff.query.all())
    #return redirect(url_for('views.view_staff'),user=current_user,staff=staff.query.all())

@views.route('/view-students-admin')
@login_required
def view_student():
    return render_template("view_student_admin.html",user=current_user, students=student.query.all())

@views.route('/view-staff')
@login_required
def view_staff():
    return render_template("view_staff.html",user=current_user, staff=staff.query.all())

@views.route('/view-students')
@login_required
def view_students():
    return render_template("view_students.html",user=current_user, students=student.query.all(), takes = takes.query.all())

@views.route('/edit-student/<int:student_id>/<Course_Code>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id, Course_Code):
    if request.method == 'POST':
        grade = request.form.get('grades')
        conn = sqlite3.connect('DBMS1/instance/College.db')
        c = conn.cursor()
        conn.execute("UPDATE takes SET grades = ? WHERE UID = ? AND Course_Code = ?", (grade, student_id, Course_Code))
        conn.commit()
        conn.close()
        return redirect(url_for('views.view_students'))
    return render_template("edit_student.html",user=current_user, takes = takes.query.all(), students = student.query.all(), student_id = student_id, Course_Code = Course_Code)

@views.route('/teacher-profile')
@login_required
def teacher_profile():
    return render_template("teacher_profile.html",user=current_user)

@views.route('/teacher-courses')
@login_required
def teacher_courses():
    return render_template("teacher_courses.html",user=current_user)

@views.route('/student-profile')
@login_required
def student_profile():
    return render_template("student_profile.html",user=current_user)

@views.route('/admin-profile')
@login_required
def admin_profile():
    return render_template("admin_profile.html",user=current_user)

@views.route('/student-courses')
@login_required
def student_courses():
    return render_template("student_courses.html",user=current_user, student=student.query.all(), takes=takes.query.all())

@views.route('/student-grades')
@login_required
def student_grades():
    return render_template("student_grades.html",user=current_user)