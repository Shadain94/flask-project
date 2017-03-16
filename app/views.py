"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash,jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import UserProfile
import time 
from datetime import date
import random
from werkzeug.utils import secure_filename
import os



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile', methods=[ "GET", "POST"])
def profile():
    
    """Render the website's about page."""
    if request.method == 'POST':
        file_folder = app.config['UPLOAD_FOLDER']
        firstname= request.form['f_name']
        image=request.files['file']
        filename = secure_filename(image.filename)
        image.save(os.path.join(file_folder, filename))
        lastname= request.form['l_name']
        username= request.form['u_name']
        userid= "6200"+str(random.randint(1,400))
        age= request.form['age']
        bio= request.form['biography']
        gender=request.form['gender_types']
        now=date.today()
        
        user= UserProfile(userid=userid,first_name=firstname, last_name=lastname, username=username, age=age, biography=bio, created_on= now.strftime('%d, %m , %Y'), gender=gender)
        db.session.add(user)
        db.session.commit()
        flash('Your information has been saved to the Database')
        return redirect(url_for('home'))

    
    return render_template('profile.html')

@app.route("/profiles", methods=["GET", "POST"])
def profiles():
    if request.method == "GET":
        ppl_info= [UserProfile.query.all()]
        images=[]
        rootdir=os.getcwd()
        for subdir, dirs, files in os.walk(rootdir + '/app/static/profile_pictures'):
            for file in files:
                images= images + [(os.path.join(file))]
        
        
        
    return render_template("profiles.html", person= ppl_info, photos=images[random.randint(0,7)])
    
@app.route("/profile/<userid>", methods=["GET","POST"])
def specific_profile(userid):
    if request.method=="GET":
        single_user=[]
        single_user = [UserProfile.query.filter_by(userid=userid).first_or_404()]
        
        images=[]
        rootdir = os.getcwd()
        for subdir, dirs, files in os.walk(rootdir + '/app/static/profile_pictures'):
            for file in files:
                images= images + [(os.path.join(file))]
        

       
        
    
        
    return render_template('show_user.html', single_person=single_user, single_image=images[random.randint(0,7)])
        
        



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")