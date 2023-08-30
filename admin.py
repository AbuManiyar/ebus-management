from mymongo import db
import logging
logging.basicConfig(filename='ebus.log', level=logging.DEBUG)


class Admin:
    def __init__(self, id, password=1234):
        logging.info('New Admin is Registering')
        try:
            admin = db[f'{id}']
            logging.info(f'New admin with id {id} registerd')
        except:
            logging.debug('Admin registration failed')
        self.id = id
        self.password = password
        admin.insert_one({'_id': f'{id}', 'password': f'{password}' })
        
        
    def createClient(self, clientID):
        
        self.clientID = clientID
        
    