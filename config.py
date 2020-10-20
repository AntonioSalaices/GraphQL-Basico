import os
class Config(object):
    SECRET_KEY="my_secret_key"
    WTF_CSRF_CHECK_DEFAULT = False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost/api_superavila'
    SQLALCHEMY_TRACK_MODIFICATIONS= True

