from dotenv import load_dotenv
import os

# Database url formation 
def sqlalchemy_connection():
    load_dotenv()
    url = "mysql+pymysql://{}:{}@{}:{}/{}".format(os.getenv('user'), os.getenv('password'), os.getenv('host'), os.getenv('port'), os.getenv('database'))
    return url
