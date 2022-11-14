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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12530103:34PprA8Jg5@sql12.freesqldatabase.com:3306/sql12530103'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from .models import User,Note
    
    
    login_manager=LoginManager()
    login_manager.login_view='auth.Login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

