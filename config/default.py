class Config(object):
    TESTING  =  False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = f"sqlite:///development.db"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database-1.cpcc3xqideqg.us-east-1.rds.amazonaws.com:5432/postgres'