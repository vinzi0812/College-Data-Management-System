#from unicodedata import category
from flask import Blueprint,render_template,flash,request,jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json
views=Blueprint('views',__name__)

@views.route('/student')
@login_required
def Student():
    return render_template("Student.html",user=current_user)