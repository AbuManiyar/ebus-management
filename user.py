from mymongo import db
import logging
logging.basicConfig(filename='ebus.log', level=logging.DEBUG)

class User:
    def register(self, firstname, lastname, email, password):
        logging.info('User is Registring')
        users = db['users']
        record = users.count_documents({'email': email})
        print(record)
        if record==0:
            users.insert_one({'firstname': firstname, 'lastname':lastname, 'email': email , 'password': password})
            logging.info('User Registered Successfully')
            return 1
        else: 
            logging.info('User mail already exist')
            return 0
   
    def login(self,email, password):
        logging.info('User is Logging in')
        users = db['users']
        record = users.find_one({'email': email})
        
        try: 
            len(record)
        except:
            logging.debug('Not a valid email')
            return 0 #'userlogin.html'
        if password == record['password']:
            return 1 #render_template('searchbus.html')
        else: 
            logging.info('Invalid Credentials')        
            return 2 #render_template('userlogin.html', msg = 'Invalid Credentials')



# below code will be transferred to application module
'''
u= User()
print(u.login("abu@gmail.com", 1234))
'''