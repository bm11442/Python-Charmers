from flask import Flask

def create_app(): 
    app = Flask(__name__)  #name of file 
    app.config['SECRET_KEY'] = 'randomString'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix= '/') #how to access
    app.register_blueprint(auth, url_prefix='/') 

    


    return app