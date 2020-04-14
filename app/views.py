"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect,abort
from app import app, db, login_manager
import os
from app.__init__ import UPLOAD_FOLDER
from flask_session import Session
from  datetime import date
import datetime
from werkzeug.datastructures import CombinedMultiDict
#from app.__init__ import UPLOAD_FOLDER
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
#from is_safe_url import is_safe_url
from werkzeug.security import check_password_hash
Usergroup = []
###
# Routing for your application.
###
now = datetime.datetime.now()

def get_profile_pic():
    form=ProfileForm()
    file = request.files.get('file')
    print(file)
            
    #filename = secure_filename(form.upload.data.filename)
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profiles", methods=["GET", "POST"])
def profiles():
     users = UserProfile.query.all()

     return render_template('profiles.html', users=users)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    filefolder = UPLOAD_FOLDER
    
    form = ProfileForm(CombinedMultiDict((request.files, request.form)))
    if request.method == "POST":
        
        if form.validate_on_submit():
        
            # Get the username and password values from the form.
            fname = form.fname.data
            lname = form.lname.data
            location = form.location.data
            email = form.email.data
            gender = form.gender.data
            bibliography = form.bibliography.data
            #file= form.photo.data
            file = request.files.get('file')
            file=form.photo.data
            if file:
                print("FILE EXISTS");
                print(form.photo.data.filename)
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(filefolder, filename))
            #file = request.files['inputFile']
            
            
            
            
            #user= UserProfile( fname, lname, location, email,bibliography,gender,file)
            user= UserProfile( fname, lname, location, email,bibliography,gender,file.filename,file.read())
            db.session.add(user)
            db.session.commit()
            flash('User Added successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash("Try again")
            print (form.errors.items())
            
    return render_template("profile.html", form=form)
    



# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))
    #return render_template('home.html')


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
    app.run(debug=True, host="0.0.0.0", port="8080")
