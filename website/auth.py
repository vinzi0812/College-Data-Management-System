from flask import Blueprint,render_template,request,flash,redirect,url_for
from .import db
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)

@auth.route('/',methods=['GET','POST'])
def Login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user,remember=True)
                return redirect(url_for('views.Student'))
    return render_template("Login.html",user=current_user)