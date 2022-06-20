from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

app = Flask(__name__, instance_relative_config=True)
scheduler = APScheduler()
csrf = CSRFProtect(app)
# scheduler.api_enabled = True
# scheduler.init_app(app)








from retroapp import config
app.config.from_object(config.ProductionConfig)
app.config.from_pyfile('config.py', silent=False)
# app.config.from_object(config.HeyConfig())



db = SQLAlchemy(app)

from retroapp.myroutes import adminroutes, userroutes, careroutes
from retroapp import forms,mymodels