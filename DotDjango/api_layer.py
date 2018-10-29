
from flaskext.mysql import MySQL
mysql=MySQL()
app.config['MYSQL_DATABASE_USER'] = 'tao'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nofuckingwaywouldsomeonehackme'
app.config['MYSQL_DATABASE_DB'] = 'Dot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
"""Write API"""
def addUser(name, email, password, first_name, last_name):
    """ Add user: all fields mandatory """
    conn=mysql.connect()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.callproc('sp_createUser',(name, email, hashed_password, first_name, last_name))

def removeUser(id):
    pass

def findUser(first_name, last_name):
    conn = mysql.connect()
    cursor = conn.cursor()
    response = cursor.query(query)

def addRating(raterID, ratedID, aspect, scale, importance, comments=None):
    conn=mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createRating', (raterID, ratedID, aspect, scale, importance, comments))

def addTeam(people):
    pass

"""Read API"""
def summerizeUser(user_id):
    pass
def query(query):
    """Query anything from the MySQL database. 
    limit=10000"""
    conn = mysql.connect()
    cursor = conn.cursor()
    response = cursor.query(query)
    return response[:1000]