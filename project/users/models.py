from project db, bcrypt

class User(db.Model):
    __tablename__ ='users' #override the table name
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_hash_password(password).decode('UTF-8')
        #The decoding on the password just ensures that our passwords are stored in the database with the proper character encoding.
