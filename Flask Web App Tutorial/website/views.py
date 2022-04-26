from flask import Blueprint, render_template

views = Blueprint('views', __name__) #blueprint for flask app, defines blue print

# Define views
@views.route('/', methods=['Get', 'POST'])  #main page of website
def home():
    return render_template("home.html")

@views.route('/about-us')
def about_us():
    return render_template("about_us.html")