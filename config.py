#import os
import os
#import load_dotenv
from dotenv import load_dotenv
#basedir assigned as operatingsystem.path.absolutepath(os.path.directoryname(__file__))
basedir = os.path.abspath(os.path.dirname(__file__))
#join basedir and '.env', use as argument for load_dotenv function
load_dotenv(os.path.join(basedir, '.env'))

#create config class
class Config():
    ''' 
        Set config variables for the flask app
        Using Environment variables where available.
        Otherwise create the config variable if not done already
    
    '''

    ##assign FLASK_APP as using the getenv method with 'FLASK_APP' as parameter on operating system
    FLASK_APP = os.getenv('FLASK_APP')
    #assign FLASK_APP as using the getenv method with 'FLASK_ENV as parameter on operating system
    FLASK_ENV = os.getenv('FLASK_ENV')
    #assign SERCRET_KEY as using the get method with parameter 'SECRET_KEY' or another string on your choosing
    SECRET_KEY = os.environ.get('SECRET_KEY' or 'There will never be another')
    #assign SQLALCHEMY_DATABASE_URI as using the get method with 'DATABASE_URI' as parameter or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI' or 'sqlite:///' + os.path.join(basedir, 'app.db')) 
    #assign SQLALCHEMY_TRACK_NOTIFICATIONS to False
    SQLALCHEMY_TRACK_NOTIFICATIONS = False