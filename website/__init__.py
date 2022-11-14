from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_login import LoginManager
db=SQLAlchemy()
#DB_NAME="users.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="yay"
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/users'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12558718:jaB7GlRJ3Y@sql12.freesqldatabase.com:3306/sql12558718'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from .models import student
    from .models import staff
    
    login_manager=LoginManager()
    login_manager.login_view='auth.Login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(UID):
        return student.query.get(int(UID))
    
    """@login_manager.user_loader
    def load_user(Teacher_Code):
        return staff.query.get(str(Teacher_Code))"""
    
    return app

