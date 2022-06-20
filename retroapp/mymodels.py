import datetime
from email import message
from email.policy import default
from turtle import back
from retroapp import db





class Admin(db.Model): 
    admin_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    admin_username = db.Column(db.String(255), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    admin_lastlogin = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow())





# #####################################################################################################################################

class User(db.Model): 
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    user_email = db.Column(db.String(255), nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_fname = db.Column(db.String(255), nullable=False)
    user_lname = db.Column(db.String(255), nullable=False)
    user_address = db.Column(db.Text(), nullable=False)
    user_gender = db.Column(db.Integer(), db.ForeignKey("gender.gender_id"), nullable=False)
    user_phone = db.Column(db.String(255), nullable=False)
    user_reg = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    state_id = db.Column(db.Integer(), db.ForeignKey("state.state_id"))

    # Creating a relationship between user and state
    states = db.relationship('State', backref='user_state')

###########################################################################################



class Userclient(db.Model): 
    client_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    client_fullname = db.Column(db.String(255), nullable=False)
    client_address = db.Column(db.Text(), nullable=False)
    client_gender = db.Column(db.Integer(), db.ForeignKey("gender.gender_id"))
    user_relationship =  db.Column(db.Text(), nullable=False)
    status_id = db.Column(db.Integer(), db.ForeignKey("status.status_id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("user.user_id"))


# Creating a relationship between user and client
    user_client = db.relationship('User', backref='client_user')

###########################################################################################




class Status(db.Model): 
    status_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    status = db.Column(db.String(255), nullable=False)
    status_price =  db.Column(db.Text(), nullable=False)


# Creating a relationship between status and client
    price = db.relationship('Userclient', backref='client_status')


###########################################################################################




class State(db.Model): 
    state_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False)




###########################################################################################



class Gender(db.Model): 
    gender_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    gender = db.Column(db.String(255), nullable=False)



# Creating a relationship between user and gender
    usergender = db.relationship('User', backref='usergender')
# Creating a relationship between client and gender
    clientgender = db.relationship('Userclient', backref='clientgender')
# ##########################################################################################


class Payment(db.Model):
    pay_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    pay_userid = db.Column(db.Integer(), db.ForeignKey("user.user_id"))
    pay_userclient_id = db.Column(db.Integer(), db.ForeignKey("userclient.client_id"))
    pay_ref = db.Column(db.String(255), nullable=False)
    pay_date = db.Column(db.Date())
    pay_status=db.Column(db.String(255), nullable=False)
    pay_amt=db.Column(db.Float())
    pay_response=db.Column(db.Text(), nullable=True)
    #set up relationship with user and userclient
    service_paid_for_who = db.relationship('Userclient', backref='pay_deets')#use backref so that we dont have to explicitly set relationship on myorder table
    user_who_paid = db.relationship('User', backref='user_payments')#available as user_payments on User table




###########################################################################################




class Booking(db.Model):
    booking_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    caregiver_id = db.Column(db.Integer(), db.ForeignKey("caregiver.care_id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("user.user_id"))
    client_id = db.Column(db.Integer(), db.ForeignKey("userclient.client_id"))
    booking_amt=db.Column(db.Float())
    pay_id = db.Column(db.Integer(), db.ForeignKey("payment.pay_id"))
    booking_start_date = db.Column(db.Date())
    booking_end_date = db.Column(db.Date())
    booking_status = db.Column(db.Enum("Ongoing","Completed" ),default="Ongoing", nullable=False)

    
# Creating a relationship between user and booking
userbook = db.relationship('User', backref='userbooking')
# Creating a relationship between client and booking
clientbook = db.relationship('Userclient', backref='clientbooking')
#  creating a relationship between caregiver and booking
carebook = db.relationship('Caregiver', backref='carebooking')
# ##########################################################################################

   


   













###########################################################################################




class Caregiver(db.Model): 
    care_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    care_email = db.Column(db.String(255), nullable=False)
    care_pass = db.Column(db.String(255), nullable=False)
    care_fname = db.Column(db.String(255), nullable=False)
    care_lname = db.Column(db.String(255), nullable=False)
    care_kin = db.Column(db.String(255), nullable=False)
    care_kin_relationship = db.Column(db.String(255), nullable=False)
    care_address = db.Column(db.Text(), nullable=False)
    care_gender = db.Column(db.Enum("male","female"), nullable=False)
    care_phone = db.Column(db.String(255), nullable=False)
    care_status = db.Column(db.Enum("pending","completed","verified"),default="pending", nullable=True)
    care_pic= db.Column(db.String(255), nullable=True)
    g_fullname1 = db.Column(db.String(255), nullable=True)
    g_address1 = db.Column(db.Text(), nullable=True)
    g_phone1 = db.Column(db.String(255), nullable=True)
    g_fullname2 = db.Column(db.String(255), nullable=True)
    g_address2= db.Column(db.Text(), nullable=True)
    g_phone2 = db.Column(db.String(255), nullable=True)
    state_id = db.Column(db.Integer(), db.ForeignKey("state.state_id"))
    care_assign_status = db.Column(db.Enum("unassigned","assigned"),default="unassigned", nullable=True)
    care_reg = db.Column(db.DateTime(), default=datetime.datetime.utcnow())



    # Creating a relationship between caregiver and state
    care_state = db.relationship('State', backref='care_location')



###########################################################################################

   