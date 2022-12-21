from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_session import Session
from os import path
db=SQLAlchemy()
DB_NAME="College.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="yay"
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/users'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12558718:jaB7GlRJ3Y@sql12.freesqldatabase.com:3306/sql12558718'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///College.db'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from .models import User,Note,student,staff,department,courses,takes, admin
    """with app.app_context():
        db.create_all()"""
    
    login_manager=LoginManager()
    login_manager.login_view='auth.Login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(Teacher_Code):
        print(session.get('key'))
        #    return student.query.get(int(Teacher_Code))
        if session.get('key') == 'student':
            return student.query.get(int(Teacher_Code))
        elif session.get('key') == 'staff':
            return staff.query.get(int(Teacher_Code))
        elif session.get('key')== 'admin':
            return admin.query.get(int(Teacher_Code))
        #return staff.query.get(int(Teacher_Code))
    
    return app

