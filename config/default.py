class Config(object):
    TESTING  =  False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///development.db"
    #SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@<server>:5432/<database>"