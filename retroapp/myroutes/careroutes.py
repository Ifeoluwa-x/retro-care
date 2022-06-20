'''This file is like the controller, it determines what the user sees, when they visit our app/routes'''
from ast import Break
from crypt import methods
import email, json , random
from multiprocessing.connection import Client
from email.headerregistry import Address
from urllib import response
from xml.etree.ElementTree import Comment
from flask import make_response, render_template, render_template_string, request, abort, redirect, flash, session,jsonify
from sqlalchemy import desc
from retroapp import app, db
from retroapp.mymodels import Gender, User, State, Caregiver,Userclient, Status,Payment,Booking
from retroapp.forms import GuarantorForm, LoginForm, ContactusForm, RegisterForm, SignUpForm
from werkzeug.security import generate_password_hash,check_password_hash




# ########################################################################################################################################



# # ########################################################################################################################################


@app.route("/care/register", methods=['GET','POST'])
def register():
    login = SignUpForm()
    if request.method == 'GET':
        state = db.session.query(State).all()
        genderdeets = db.session.query(Gender).all()
        return render_template('/care/register.html' ,login = login, state = state, genderdeets = genderdeets)
    else:
        #retrieve form data  
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        next_of_kin = request.form.get('kin')
        address = request.form.get('add')
        relationship_with_kin = request.form.get('relakin')
        state = request.form.get('state')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        fname1 = request.form.get('fname1')
        add1 = request.form.get('add1')
        phone1 = request.form.get('phone1')
        fname2 = request.form.get('fname1')
        add2 = request.form.get('add2')
        phone2 = request.form.get('phone2')

        # Final form or validation after using flask form
        if state == '' or gender =='': 
            state = db.session.query(State).all()
            genderdeets = db.session.query(Gender).all()
            flash("Choose your location and gender")
            return render_template('/care/register.html' ,login = login, state = state , genderdeets = genderdeets)
        else:

            pwd= generate_password_hash(pwd)
            # Inserting data retrieved into the database
            c = Caregiver(care_email=email,
            care_pass=pwd,
            care_fname=fname, 
            care_lname=lname, 
            care_address = address,
            care_gender = gender,
            care_phone = phone,
            care_kin = next_of_kin,
            g_fullname1=fname1,
            g_address1 = add1,
            g_phone1 = phone1,
            g_fullname2=fname2,
            g_address2 = add2,
            g_phone2 = phone2,
            care_kin_relationship = relationship_with_kin,
            state_id = state)
            db.session.add(c)
            db.session.commit()
            id = c.care_id
            session['loggedin'] = id
        return redirect('/care/login/here')



@app.route("/care/login/here", methods=['GET'])
def login_here():
    return render_template("/care/loginhere.html")




@app.route('/care/login', methods=['POST', 'GET']) 
def login():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('care/login.html', login=login)
    else:
        '''We retrieve the form data'''
        username = request.form.get('username') #method1
        # pwd = login.pwd.data #method 2
        pwd =  request.form.get('pwd')
        # validate
        if login.validate_on_submit():
            deets = Caregiver.query.filter(Caregiver.care_email==username).first()
            if deets:
                formattedpwd = deets.care_pass
                checkpwd = check_password_hash(formattedpwd,pwd)
                if checkpwd:
                    #retrieve user's id and then keep in session , we still use the same loggedin session we use below both are trying to log the user in
                    id = deets.care_id
                    session['loggedin']=id
                    return redirect('/care/profile')
                else:
                    flash('Username or password is incorrect')
                return redirect('/care/login')
            else:
        
                flash('Username or password is incorrect')
                return f"{deets}"#redirect('/care/login')
        else:
            return render_template('care/login.html', login=login)




@app.route('/care/profile', methods=['GET'])
def profile():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/")
    else:
        caredeets = db.session.query(Caregiver).get(loggedin)
        return render_template('/care/profile.html', caredeets = caredeets)


# This function helps project more information on a caregiver
@app.route('/care/more')
def care_more():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/")
    else:
        caredeets = Caregiver.query.get(loggedin)
        subdeets = db.session.query(Caregiver, Booking, Userclient). \
                select_from(Caregiver).join(Booking).join(Userclient).filter(Caregiver.care_id==loggedin).all()
        len_of = len(subdeets)
        deets = db.session.query(Booking,Caregiver , Userclient). \
                select_from(Booking).join(Caregiver).join(Userclient).filter(Booking.caregiver_id==loggedin,Booking.booking_status== "Ongoing" ).all()
        return render_template('/care/more.html', caredeets = caredeets , subdeets= subdeets, len_of = len_of, deets = deets)  # caredeets=caredeets





@app.route('/care/profileinfo', methods=['GET'])
def profileinfo():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/")
    else:
        caredeets = db.session.query(Caregiver).get(loggedin)
        return render_template('/care/profileinfo.html', caredeets = caredeets)





@app.route('/care/history', methods=['GET'])
def care_history():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/care/login")
    else:
        caredeets = db.session.query(Caregiver).get(loggedin)
        subdeets = db.session.query(Caregiver, Booking, Userclient). \
            select_from(Caregiver).join(Booking).join(Userclient).filter(Caregiver.care_id==loggedin).all()
        return render_template('care/history.html', caredeets=caredeets , subdeets = subdeets)



@app.route('/care/reward', methods=['GET'])
def care_reward():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/care/login")
    else:
        caredeets = db.session.query(Caregiver).get(loggedin)
        return render_template('care/reward.html', caredeets=caredeets)



@app.route('/care/resetpassword', methods=['GET','POST'])
def care_reset():
    loggedin = session.get('loggedin')
    caredeets = db.session.query(Caregiver).get(loggedin)
    
    if loggedin == None:
        return redirect("/user/login")
    if request.method == 'GET':
        return render_template("/care/change_password.html", caredeets=caredeets)
    else:
        caredeets = db.session.query(Caregiver).get(loggedin)
        # Retrieve data from form
        oldpwd = request.form.get('oldpwd')
        newpwd1 = request.form.get('newpwd1')
        newpwd2 = request.form.get('newpwd2')
        formattedpwd = caredeets.care_pass
        checkpwd = check_password_hash(formattedpwd,oldpwd)
        if checkpwd:
            if oldpwd == '' or newpwd1 == '' or newpwd2 == '':
                flash('Please fill in the fields')
            elif newpwd1 != newpwd2:
                flash('Please make sure both passwords match')
            else:
                newpwd1 = generate_password_hash(newpwd1)
                caredeets.care_pass=newpwd1
                db.session.commit()
                return redirect('/care/changed')
        else:
            flash('Your old password is in correct')
            caredeets = db.session.query(Caregiver).get(loggedin)
            return render_template('care5/change_password.html', caredeets = caredeets)





@app.route('/care/changed', methods=['GET','POST'])
def changed():
    loggedin = session.get('loggedin')
    caredeets = db.session.query(Caregiver).get(loggedin)
    if loggedin == None:
        return redirect("/user/login")
    else:
        return render_template("care/changed.html", caredeets = caredeets)
