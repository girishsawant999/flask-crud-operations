from flask import Flask, request, render_template

import DatabaseOperations
import TestCode

app = Flask(__name__)

app.secret_key = "admin@123"

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/loginCustomerHelp')
def loginCustomerHelp(msg="Sign in to continue.", email=''):
    return render_template('loginCustomer.html', msg=msg, email=email)


@app.route('/loginCustomer', methods=['POST'])
def loginCustomer():
    email, password = "", ""
    if request.method == 'POST':
        email, password = request.form['email'], request.form['pass']
        if TestCode.checkMailFail(email):
            return loginCustomerHelp("Email Constraint Failed.")
    data = DatabaseOperations.checkCustomerData(email)
    if data == (): return loginCustomerHelp("User Not Found.")
    if password != data[1]:
        return loginCustomerHelp("Password Invalid.", email)
    else:
        return "Login Succesfully.."


@app.route('/loginDriverHelp')
def loginDriverHelp(msg="Sign in to continue.", email=''):
    return render_template('loginDriver.html', msg=msg, email=email)


@app.route('/loginDriver', methods=['POST'])
def loginDriver():
    email, password = "", ""
    if request.method == 'POST':
        email, password = request.form['email'], request.form['pass']
        if TestCode.checkMailFail(email):
            return loginDriverHelp("Email Constraint Failed.")
    data = DatabaseOperations.checkDriverData(email)
    if data == (): return loginDriverHelp("User Not Found.")
    if password != data[1]:
        return loginDriverHelp("Password Invalid.", email)
    else:
        return "Login Succesfully.."


@app.route('/regCustomerHelp')
def regCustomerHelp(msg="Register Here", name='', address='', contact='', email=''):
    return render_template('regCustomer.html', msg=msg, name=name, address=address, contact=contact, email=email)


@app.route('/regCustomer', methods=['POST'])
def regCustomer():
    if request.method == 'POST':
        if request.form['choice'] == 'Cancel': return root()

        name, gender, address = request.form['name'], request.form['gender'], request.form['add']
        contact, email, password = request.form['contact'], request.form['email'], request.form['pass']

        if TestCode.checkNameFail(name):
            return regCustomerHelp("Name Constraint Failed (Max 30 AlphaChars)", '', address, contact, email )
        if TestCode.checkMailFail(email):
            return regCustomerHelp("Email Constraint Failed (Max 30 Chars)", name, address, contact, '')
        if DatabaseOperations.checkCustomerData(email):
            return loginCustomerHelp("User Already Present, Login.", email)
        if TestCode.checkContactFail(contact):
            return regCustomerHelp("Invalid Contact Details", name, address, '', email)
        if TestCode.checkPasswordFail(password):
            return regCustomerHelp("Password Constraint Failed (Max 20 chars without space)", name, address, contact,
                                   email)
        if TestCode.checkAddressFail(address):
            return regCustomerHelp("Address Constraint Failed (Max 40 Chars)", name, '', contact, email)

        DatabaseOperations.insertCustomerData(address, contact, email, gender, name, password)
    return '''Done...'''


@app.route('/regDriverHelp')
def regDriverHelp(msg="Register Here", name='', address='', contact='', email='', licence=''):
    return render_template('regDriver.html', msg=msg, name=name, address=address, contact=contact, email=email,
                           licence=licence)


@app.route('/regDriver', methods=['POST'])
def regDriver():
    if request.method == 'POST':
        if request.form['choice'] == 'Cancel': return root()
        name, gender, address = request.form['name'], request.form['gender'], request.form['add']
        contact, email, password = request.form['contact'], request.form['email'], request.form['pass']
        status, licence = request.form['status'], request.form['licence']

        if TestCode.checkNameFail(name):
            return regDriverHelp("Name Constraint Failed (Max 30 AlphaChars)", '', address, contact, email, licence)
        if TestCode.checkMailFail(email):
            return regDriverHelp("Email Constraint Failed (Max 30 Chars)", name, address, contact, '', licence)
        if DatabaseOperations.checkDriverData(email):
            return loginDriverHelp("User Already Present, Login.", email)
        if TestCode.checkContactFail(contact):
            return regDriverHelp("Invalid Contact Details", name, address, '', email, licence)
        if TestCode.checkPasswordFail(password):
            return regDriverHelp("Password Constraint Failed (Max 20 chars without space)", name, address, contact,
                                 email, licence)
        if TestCode.checkAddressFail(address):
            return regDriverHelp("Address Constraint Failed (Max 40 Chars)", name, '', contact, email, licence)
        if TestCode.checkLicenceFail(licence):
            pass

        DatabaseOperations.insertDriverData(address, contact, email, gender, licence, name, password, status)
    return '''Done..'''


# def regVechile():
#     pass
#
#
# def regOrder():
#     pass
#
#
# def allDatabase():
#     pass
#

if __name__ == '__main__':
    app.run(debug=True)
