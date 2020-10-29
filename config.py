import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # It has to be called SQLALCHEMY_DATABASE_URI

    SECRET_KEY = "chocolate"

    


