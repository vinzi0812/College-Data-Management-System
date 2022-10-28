#from unicodedata import category
from flask import Blueprint,render_template,flash,request,jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json
views=Blueprint('views',__name__)

@views.route('/student-profile')
@login_required
def student_profile():
    return render_template("student_profile.html",user=current_user)

@views.route('/student-courses')
@login_required
def student_courses():
    return render_template("student_courses.html",user=current_user)

@views.route('/student-grades')
@login_required
def student_grades():
    return render_template("student_grades.html",user=current_user)