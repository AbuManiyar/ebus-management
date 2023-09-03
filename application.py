from flask import Flask,render_template,request
import logging
logging.basicConfig(filename='ebus.log', level=logging.DEBUG)
from user import User  
from admin import Admin 
from driver import Driver


application =  Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/adminlogin')
def adminlogin():
   return render_template('adminlogin.html') 
   

@application.route('/admin', methods = ['POST'])
def admin():
    id = request.form['ID']
    password = request.form['Password']
    a = Admin(id,password)
    result = a.login()
    if result ==1:
        agency = a.agency()
        return render_template('admin.html', agency = agency, adminid = id)
    elif result==0:
        return render_template('adminlogin.html', msg = 'Wrong Admin Id')
    else: 
        return render_template('adminlogin.html', msg = 'Invalid Credentials')

@application.route('/createdriver/<adminid>', methods=["POST"])
def createdriver(adminid):
    driver = request.form['DID']
    password = request.form['Password']
    add = Admin.createdriver(adminid,driver,password)
    if add == 0:
        return render_template('admin.html', adminid=adminid, msg='Driver Already Exist')
    elif add==1:
        return render_template('admin.html', adminid=adminid, msg='Driver Added')
    else:
        return 'Some error occured'


if __name__ == '__main__':
    application.run(debug=True)