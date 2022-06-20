'''This file is like the controller, it determines what the user sees, when they visit our app/routes'''
import math, random, os #imported at the top cos it's from python
from flask import make_response, render_template, request, abort, redirect, flash, session, url_for,jsonify
from retroapp import app, db
from retroapp.mymodels import Payment, User, Admin,Caregiver,Booking,Userclient
from retroapp.forms import LoginForm
from sqlalchemy import func, or_,bindparam


@app.route('/admin/login', methods=['GET'])
def adminlogin():
    login = LoginForm()
    return render_template('admin/login.html', login = login)




@app.route('/admin/submit/login', methods=['POST'])
def submit_adminlogin():
    username = request.form.get('username')
    pwd = request.form.get('pwd')

    if username == '' or pwd == '':
        flash('Please complete all fields')
        return redirect(url_for('adminlogin'))
    else:
        admindeets = Admin.query.filter(Admin.admin_username==username, Admin.admin_password==pwd).first()

        if admindeets:
            admin_id = admindeets.admin_id 
            session['admin_id'] = admin_id

            flash('Login Successful')
            return redirect('/adminpage')
        else:
            flash('Invalid Credentials')   
            return redirect('/admin/login') 





@app.route('/adminpage')
def admin_profile():
    admin_id = session.get('admin_id')
    admindeets =  db.session.query(Admin).get(admin_id)
    return render_template('admin/index.html', admindeets = admindeets)



@app.route('/admin/caregivers/', methods=['GET','POST'])
def caregivers():
    admin_id = session.get('admin_id')
    if admin_id == None: 
        return redirect('/admin/login')
    else:
        caredeets = Caregiver.query.all()
        return render_template('admin/caregiver.html', caredeets = caredeets)


@app.route('/admin/caregivers/search', methods=['GET','POST'])
def caregivers_search():
    admin_id = session.get('admin_id')
    if admin_id == None: 
        return redirect('/admin/login')
    else:
        # Retrieve the form
        carename = request.form.get('search_text')
        caredets = Caregiver.query.filter(func.concat(Caregiver.care_fname, " " ,Caregiver.care_lname).like('%{0}%'.format(carename))).all()
        return render_template('admin/caregiver_search.html', caredets = caredets)



@app.route('/admin/upload/<care_id>', methods=['POST'])
def admin_upload(care_id):
    #request file
    pic_object = request.files.get('img')
    # return f"{pic_object}"
    original_file =  pic_object.filename
    if original_file != '': #check if file is not empty
        extension = os.path.splitext(original_file)
        if extension[1].lower() in ['.jpg','.png']:
            fn = math.ceil(random.random() * 100000000)  
            save_as = str(fn)+extension[1]
            pic_object.save(f"retroapp/static/assets/img/{save_as}")
            #insert other details into db
            b = Caregiver.query.get(care_id)
            b.care_pic = save_as
            db.session.add(b)
            db.session.commit()            
            return redirect("/admin/caregivers")
        else:
            flash('File Not Allowed')
            return redirect("/admin/caregivers")

    else:
        flash('Process failed. Try again!')          
        return "empty"#redirect("/admin/caregivers")

# This function helps project more information on a caregiver
@app.route('/admin/more/<id>')
def admin_more(id):
    b = Caregiver.query.get(id)
    subdeets = db.session.query(Caregiver, Booking, Userclient). \
            select_from(Caregiver).join(Booking).join(Userclient).filter(Caregiver.care_id==id).all()
    lenof = len(subdeets)
    return render_template('/admin/more.html', b = b , subdeets= subdeets, lenof = lenof)   





# The function that deals with the verification of a care giver
@app.route('/admin/verify/<id>')
def admin_verify(id):
    b = Caregiver.query.get(id)
    b.care_status = "verified"
    db.session.commit()  
    return redirect('/admin/caregivers')  







@app.route('/admin/users')
def admin_users():
    userdeets = User.query.all()
    return render_template('/admin/users.html', userdeets=userdeets)  


@app.route('/admin/users/search', methods=['GET','POST'])
def users_search():
    admin_id = session.get('admin_id')
    if admin_id == None: 
        return redirect('/admin/login')
    else:
        # Retrieve the form
        username = request.form.get('search_text')
        # Query the database
        userdeets = User.query.filter(func.concat(User.user_fname, " " ,User.user_lname).like('%{0}%'.format(username))).all()
        return render_template('admin/user_search.html', userdeets = userdeets)



# This function helps project more information on a user
@app.route('/admin/user/more/<id>')
def admin_user_more(id):
    b = User.query.get(id)
    deets = db.session.query(User, Booking, Userclient, Caregiver). \
            select_from(User).join(Booking).join(Userclient).join(Caregiver).filter(User.user_id==id).all()
    paydeets = db.session.query(User, Payment, Userclient). \
            select_from(User).join(Payment).join(Userclient).filter(User.user_id==id).all()
    return render_template('/admin/usermore.html', b = b , deets= deets ,paydeets = paydeets)    






# @app.route('/admin/breakout/delete/<breakid>')
# def admin_deletebreakout(breakid):
#     b = Breakout.query.get(breakid)
#     db.session.delete(b)
#     db.session.commit()
#     flash(f'Breakout session {id} deleted')
#     return redirect('/admin/breakout')

@app.route('/admin/logout')    
def admin_logout():
    admin_id = session.get('admin_id')
    if admin_id == None: 
        return redirect('/admin/login')
    session.pop('admin_id')    
    return redirect('/admin/login')