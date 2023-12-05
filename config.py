#import os
#import load_dotenv
#basedir assigned as operatingsystem.path.absolutepath(os.path.directoryname(__file__))
#join basedir and '.env', use as argument for load_dotenv function

#create config class
    ''' 
    
    
    '''

    ##assign FLASK_APP as using the getenv method with 'FLASK_APP' as parameter on operating system
    #assign FLASK_APP as using the getenv method with 'FLASK_ENV as parameter on operating system
    #assign SERCRET_KEY as using the get method with parameter 'SECRET_KEY' or another string on your choosing
    #assign SQLALCHEMY_DATABASE_URI as using the get method with 'DATABASE_URI' as parameter or 'sqlite:///' + os.path.join(basefir, 'app.db')
    #assign SQLALCHEMY_TRACK_NOTIFICATIONS to False