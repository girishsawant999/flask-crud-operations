def checkContactFail(contact):
    if len(contact) != 10 or not contact.isdigit() or contact == '':
        return True
    else:
        return False


def checkAddressFail(address):
    if len(address) > 40 or address == '':
        return True
    else:
        return False


def checkNameFail(name):
    if len(name) > 30 or name == '':
        return True
    for word in name.split():
        if not word.isalpha():
            return True
    return False


def checkMailFail(email):
    if len(email) > 30 or email == '':
        return True
    else:
        return False


def checkPasswordFail(password):
    if len(password) > 20 or password == '':
        return True
    if ' ' in password:
        return True
    return False


def checkLicenceFail(licence):
    pass
