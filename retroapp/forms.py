from email import message
from email.headerregistry import Address
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, RadioField

from wtforms.validators import DataRequired, Email, EqualTo,Length,Regexp



class LoginForm(FlaskForm):
    username = StringField('Your Email:', validators=[
                           DataRequired(), 
                           Email()])
    # message argument here allows you to specify a custom message if the user does not do what is expected of them, e.g fill a form field incorrectly
    pwd = PasswordField('Enter password:')
    # example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])
    loginbtn = SubmitField('Login')

    

class ContactusForm(FlaskForm):
    message = TextAreaField('Your message:' )
    email = StringField('Your Email:', validators=[DataRequired(), Email()])
    fullname = StringField('Your Name:', validators=[DataRequired()])
    loginbtn = SubmitField('Login')



class RegisterForm(FlaskForm):
    fname = StringField('Your firstname:', validators=[ DataRequired()])
    lname = StringField('Your lastname:', validators=[ DataRequired()])
    email = StringField('Your Email:', validators=[DataRequired(), Email()])
    add =  StringField('Your Address:', validators=[DataRequired()])
    phone = StringField('Your Phone no:', validators=[ DataRequired()])
    pwd = PasswordField('Enter password:', validators=[ DataRequired(), Length(min=5, max=35, message="Password must be between 4 and 35 characters")])
    loginbtn = SubmitField('Sign Up')
    


class ResetpassForm(FlaskForm):
    oldpwd = PasswordField('Enter password:', validators=[ DataRequired()])
    newpwd = PasswordField('Enter password:', validators=[ DataRequired(), EqualTo('confirm', message='Passwords must match')]) 
    newpwd2 = PasswordField('Confirm password:', validators=[ DataRequired()])



class SignUpForm(FlaskForm):
    fname = StringField('Your firstname:', validators=[ DataRequired()])
    lname = StringField('Your lastname:', validators=[ DataRequired()])
    email = StringField('Your Email:', validators=[DataRequired(), Email()])
    add =  StringField('Your Address:', validators=[DataRequired()])
    phone = StringField('Your Phone no:', validators=[ DataRequired()]) 
    pwd = PasswordField('Confirm password:', validators=[ DataRequired(),  Length(min=5, max=35, message="Password must be between 4 and 35 characters")])
    kin =  StringField('Your Next of kin:', validators=[DataRequired()])
    relakin =  StringField('Your Next of kin:', validators=[DataRequired()])
    fname1 = StringField('Guarantor firstname:', validators=[ DataRequired()])
    add1 =  StringField('Your Address:', validators=[DataRequired()])
    phone1 = StringField('Your Phone no:', validators=[ DataRequired()])
    fname2 = StringField('Your firstname:', validators=[ DataRequired()])
    add2 =  StringField('Your Address:', validators=[DataRequired()])
    phone2 = StringField('Your Phone no:', validators=[ DataRequired()]) 
    loginbtn = SubmitField('Sign Up')


class GuarantorForm(FlaskForm):
    fname1 = StringField('Guarantor firstname:', validators=[ DataRequired()])
    add1 =  StringField('Your Address:', validators=[DataRequired()])
    phone1 = StringField('Your Phone no:', validators=[ DataRequired()])
    fname2 = StringField('Your firstname:', validators=[ DataRequired()])
    add2 =  StringField('Your Address:', validators=[DataRequired()])
    phone2 = StringField('Your Phone no:', validators=[ DataRequired()]) 
    loginbtn = SubmitField('Sign Up')