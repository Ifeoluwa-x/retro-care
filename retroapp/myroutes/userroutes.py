'''This file is like the controller, it determines what the user sees, when they visit our app/routes'''
import re
from ast import Break
from crypt import methods
from sqlalchemy import func
from datetime import date #This can be done at the top of the module
import email, json , random, requests, datetime,time
from turtle import undobufferentries
from http import client
from multiprocessing.connection import Client
from email.headerregistry import Address
from urllib import response
from xml.etree.ElementTree import Comment
from flask import make_response, render_template, request, abort, redirect, flash, session,jsonify
from sqlalchemy import desc
from retroapp import app, db
from retroapp.mymodels import User, State, Caregiver,Userclient, Status,Payment, Gender,Booking
from retroapp.forms import LoginForm, ContactusForm, RegisterForm, SignUpForm
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from werkzeug.security import generate_password_hash,check_password_hash















# This is the home route
@app.route("/")
def home():
    return render_template("user/retro.html")


@app.route("/user/signup", methods=['POST', 'GET'])
def signup():
    login = RegisterForm()
    if request.method == 'GET':
        states = db.session.query(State).all()
        genderdeetss = db.session.query(Gender).all()
        return render_template('/user/signup.html' ,login = login, states = states, genderdeetss = genderdeetss)
    else:
        if login.validate_on_submit():
            #retrieve form data
            email = request.form.get('email')
            pwd = request.form.get('pwd')
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            address = request.form.get('add')
            state = request.form.get('state')
            phone = request.form.get('phone')
            gender = request.form.get('gender')



            pwd= generate_password_hash(pwd)
            u = User(user_email=email,
                        user_pass=pwd,
                        user_fname=fname, 
                        user_lname=lname, 
                        user_gender = gender,
                        user_address = address,
                        user_phone = phone,
                        state_id = state)
            db.session.add(u)
            db.session.commit()
            id = u.user_id
            session['loggedin'] = id
            return redirect('/user/profile')
        states = db.session.query(State).all()
        genderdeetss = db.session.query(Gender).all()
        return render_template("/user/signup.html" , login = login, states = states, genderdeetss = genderdeetss)
            



@app.route('/user/login', methods=['POST', 'GET']) 
def submit_login():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('user/login.html', login=login)
    else:
        '''We retrieve the form data'''
        username = request.form.get('username') #method1
        # pwd = login.pwd.data #method 2
        pwd =  request.form.get('pwd')
        # validate
        if login.validate_on_submit():
            deets = User.query.filter(User.user_email==username).first()
            if deets:
                formattedpwd = deets.user_pass
                checkpwd = check_password_hash(formattedpwd,pwd)
                if checkpwd:
                    #retrieve user's id and then keep in session , we still use the same loggedin session we use below both are trying to log the user in
                    id = deets.user_id
                    session['loggedin']=id
                
                    return redirect('/user/profile')
                else:
                    flash('Username or password incorrect')
                    return redirect('/user/login')
            else:
                flash('Username or password incorrect')
                return redirect('/user/login')
        else:
            return render_template('user/login.html', login=login)


@app.route('/user/profile', methods=['GET','POST'])
def user_profile():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/user/login")
    else:
        userdeets = db.session.query(User).get(loggedin)
        return render_template('user/profile.html', userdeets=userdeets)


@app.route('/user/logout', methods=['GET','POST'])
def logout():
    session.pop('loggedin')
    return redirect('/')



@app.route('/user/manage', methods=['GET','POST'])
def user_manage():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/user/login")
    else:
        userdeets = db.session.query(User).get(loggedin)
        return render_template('user/manage_service.html', userdeets=userdeets)




@app.route('/user/history', methods=['GET','POST'])
def user_history():
    loggedin = session.get('loggedin')
    
    if loggedin == None:
        return redirect("/user/login")
    else:
        userdeets = db.session.query(User).get(loggedin)


        bookdeets = db.session.query(User, Booking, Userclient, Caregiver). \
            select_from(User).join(Booking).join(Userclient).join(Caregiver).filter(User.user_id==loggedin).all()
        return render_template('user/history.html', userdeets=userdeets, bookdeets = bookdeets ,client =client)


@app.route('/user/client', methods=['GET','POST'])
def user_client():
    loggedin = session.get('loggedin')
    userdeets = db.session.query(User).get(loggedin)
    status = db.session.query(Status).all()
    gender = db.session.query(Gender).all()
    if loggedin == None:
        return redirect("/user/login")
    if request.method == 'GET':
        status = db.session.query(Status).all()
        return render_template('user/client.html', userdeets=userdeets, status= status, gender = gender)
    else:
        #retrieve form data
        fullname = request.form.get('fullname')
        address = request.form.get('address')
        genderid = request.form.get('gender')
        relationship = request.form.get('client_rela')
        status = request.form.get('status')
        if fullname == '' or relationship == '' or address == '' or status == '' or gender == "":
            flash('Please complete all fields')
            
            
            return redirect('/user/client')
        else:
            u = Userclient(client_fullname=fullname,
            user_relationship=relationship,
            client_address=address,
            status_id=status,
            user_id=loggedin, 
            client_gender =genderid)
            # db.session.execute(f"INSERT INTO userclient SET client_fullname='{fullname}', user_relationship='{relationship}', client_address='{address}', status_id='{status}', user_id='{loggedin}', client_gender = '{genderid}'")
            db.session.add(u)
            db.session.commit()
            id = u.client_id
            session['logged'] = id
            return redirect('/user/confirm/payment')






@app.route('/user/confirm/payment', methods=['GET','POST'])
def confirm_payment():
    loggedin = session.get('loggedin')
    logged = session.get('logged')
    userdeets = db.session.query(User).get(loggedin)
    clientdeets = db.session.query(Userclient).filter(Userclient.user_id==userdeets.user_id).order_by(desc(Userclient.client_id)).first()
    hey = Status.query.filter(Status.status_id == clientdeets.status_id ).first()
    if loggedin == None:
        return redirect("/user/login")
    if request.method == 'GET':
        return render_template('user/confirm_payment.html', userdeets=userdeets, clientdeets=clientdeets,hey=hey)
    else:
        ref = int(random.random() * 10000000)
        session['refno']= ref
        data = {"email":userdeets.user_email, "amount":hey.status_price}
        headers = {"Content-Type": "application/json","Authorization": "Bearer sk_test_80ae30524f47afdfed963d1e4d434285a39d68cd"}
        response = requests.post('https://api.paystack.co/transaction/initialize', headers = headers, data= json.dumps(data))
        rspjson = json.loads(response.text)
        if rspjson.get("status") == True:
            authurl = rspjson["data"]["authorization_url"]
            return redirect(authurl)
        else:
            "please try again"



@app.route('/user/paystack')
def paystack():
    user = session.get('loggedin')
    loggedin = session.get('loggedin')
    logged = session.get('logged')
    userdeets = db.session.query(User).get(loggedin)
    clientdeets = db.session.query(Userclient).filter(Userclient.user_id==userdeets.user_id).order_by(desc(Userclient.client_id)).first()
    ref = session.get("refno")
    reference = request.args.get('reference')
    #update db
    headers = {"content-Type":"application/json", "Authorization": "Bearer sk_test_80ae30524f47afdfed963d1e4d434285a39d68cd"}
    response = requests.get(f"https://api.paystack.co/transaction/verify/{reference}", headers=headers)
    rsp=response.json()
    if rsp['data']['status'] == "success":
        amount = rsp['data']['amount']
        method = rsp['data']['channel']
        currency = rsp['data']['currency']
        status ="successful"
        now = datetime.datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        p = Payment(pay_userid=loggedin,
                    pay_userclient_id = clientdeets.client_id,
                    pay_ref = ref,
                    pay_date =date_string,
                    pay_status =status,
                    pay_amt = amount
                    )
        db.session.add(p)
        db.session.commit()
        id = p.pay_id
        session['paymentsess'] = id

        return redirect('payment/successful')
    else:  
        status ="failed"
        payment = Payment(pay_userid=loggedin,
                    pay_userclient_id = clientdeets.client_id,
                    pay_ref = reference,
                    pay_status =status,
                    pay_amt = amount
                    )
        db.session.add(payment)
        db.session.commit()
        return "payment failied"




@app.route('/user/payment/successful', methods=['GET','POST'])
def payment_sus():
    loggedin = session.get('loggedin')
    logged = session.get('logged')
    paymentsess = session.get('paymentsess')
    if loggedin == None:
        return redirect("/user/login")
    else:
        # Select from the database where a caregiver is verified and currently unassigned to a user
        caredeets = db.session.query(Caregiver).filter(Caregiver.care_status == "verified",Caregiver.care_assign_status == "unassigned").first()
        id = caredeets.care_id
        session['caresess'] = id
        c = Caregiver.query.get(id)
        c.care_assign_status = "assigned"
        db.session.commit()  

        userdeets = db.session.query(User).get(loggedin)
        paydeets = db.session.query(Payment).get(paymentsess)
        start_date = datetime.timedelta(days = 1)
        end_date = datetime.timedelta(days = 30)
        
        #inserting into database
        b = Booking(caregiver_id = caredeets.care_id,
                    user_id = loggedin,
                    client_id = logged,
                    booking_amt = paydeets.pay_amt,
                    pay_id = paydeets.pay_id,
                    booking_start_date = paydeets.pay_date + start_date,
                    booking_end_date = paydeets.pay_date + end_date,
                    booking_status = "Ongoing")
        db.session.add(b)
        db.session.commit()
        id = b.booking_id
        session['booksess'] = id
        # Then i'm supposed to run a scheduled task below on the booking end date. #I've tried different approach such as cron job and apscheduler
        # None seems to work for me. 
        # def scheduled_task():
        #     caresess = session.get('caresess')
        #     booksess = session.get('booksess')
        #     paymentsess = session.get('paymentsess')
        #     logged = session.get('logged')
        #     loggedin = session.get('loggedin')
        #     # Updating the  booking session to be completed
        #     complete_session =  db.session.query(Booking).filter(Booking.booking_id == "booksess").first()
        #     complete_session.booking_status = "completed"
        #     db.session.commit()  

        #     # Updating the caregive assign status to "Unassigned" to be available to other users after the end of the session.
        #     update_status =  db.session.query(Caregiver).filter(Caregiver.care_id == "caresess").first()
        #     update_status.care_assign_status = "unassigned"
        #     db.session.commit()  


        return redirect('/endjob')

@app.cli.command()
def end_job():
    """ Run oh faqrrrrrrr"""
    # caresess = session.get('caresess')
    # booksess = session.get('booksess')
    # paymentsess = session.get('paymentsess')
    # logged = session.get('logged')
    # loggedin = session.get('loggedin')
    # complete_session = db.session.query(Booking).filter(
    # func.date(Booking.booking_end_date) == date.today().strftime('%Y-%m-%d')).all()
    print('My name is ifeoluwa')
    # In a loop, update the status of each of these bookings to unassigned
    # Updating the caregiver assign status to "Unassigned" to be available to other users after the end of the session.
    # return ("Done!!!")

























@app.route('/user/reward', methods=['GET','POST'])
def user_reward():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/user/login")
    else:
        userdeets = db.session.query(User).get(loggedin)
        return render_template('user/reward.html', userdeets=userdeets)



@app.route('/user/resetpassword', methods=['GET','POST'])
def user_reset():
    loggedin = session.get('loggedin')
    if loggedin == None:
        return redirect("/user/login")
    if request.method == "GET":
        userdeets = db.session.query(User).get(loggedin)
        return render_template('user/change_password.html', userdeets=userdeets)
    else:
        userdet = db.session.query(User).get(loggedin)
        # Retrieve data from form
        oldpwd = request.form.get('oldpwd')
        newpwd1 = request.form.get('newpwd1')
        newpwd2 = request.form.get('newpwd2')
        # comparing password input and formatted password
        formattedpwd = userdet.user_pass
        checkpwd = check_password_hash(formattedpwd,oldpwd)
        if checkpwd:
            if oldpwd == '' or newpwd1 == '' or newpwd2 == '':
                flash('Please fill in the fields')
            elif newpwd1 != newpwd2:
                flash('Please make sure both passwords match')
            else:
                newpwd1= generate_password_hash(newpwd1)
                userdet.user_pass=newpwd1
                db.session.commit()
                flash('Your password has been successfully changed!')
        else:
            flash('Your old password is in correct')
        userdeets = db.session.query(User).get(loggedin)
        return render_template('user/change_password.html', userdeets=userdeets)


########################################################################################################################################