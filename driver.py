from mymongo import db
import logging
logging.basicConfig(filename='ebus.log', level=logging.DEBUG)


'''
Driver/Travels:
Login:
    Drivers/Travels are login to this system.
Post Bus Information:
    Drivers/Travels enter this system and post their Bus's complete Information.
Post Bust Type:
    Drivers/Travels enter this system and post their Bus's complete details about type of bus.
Post Contact:
    Drivers/Travels enter this system and post their Contact details.
'''


class Driver:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        
        
    def login(self):
        drivers =  db['driver']
        detail = drivers.find_one({'driver id': self.id})
        try: 
            print(len(detail))
            print('try block in login')
        except:
            logging.info('no matching id for driver')
            return 0
        if self.password == detail['password'] :
            logging.info('driver logged in')
            return 1
        else :
            logging.info('invalid password for driver')
            return 2
        
    def postbusinfo(self, type, contact, *info):
       try:
        bus = db['bus']
        details = {'driver id': self.id, 'info': info, 'type' : type, 'contact': contact }
        bus.insert_one(details)
        logging.info('Bus info added')
        return 1
       except:
           logging.info('Bus info addition failed')
           return 0
       
       
#this similar code moves to application module
'''
d=Driver('driver2', 'password2')
print(d.login())
'''