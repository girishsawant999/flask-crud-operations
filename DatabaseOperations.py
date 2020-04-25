import sqlite3 as sql
from datetime import datetime


def errorWrite(err, tb):
    f = open("ErrorFile.txt", "a")
    f.writelines(datetime.now().strftime("%d-%m-%Y : %H:%M:%S : ") + tb + " : " + err + '\n')
    f.close()


def insertCustomerData(address, contact, email, gender, name, password):
    con = sql.connect("ProjectDatabase.db")
    try:
        ref = con.cursor()
        ref.execute(
            'CREATE TABLE IF NOT EXISTS Customers(CId INTEGER PRIMARY KEY AUTOINCREMENT,CName Varchar(30),'
            'CGender char(6) ,CAdd varchar(40),CContact char(10),'
            'CEmail varchar(30),CPassword varchar(20))')
        query = "INSERT INTO Customers (CName,CGender,CAdd,CContact,CEmail,CPassword) VALUES ('" + name + "','" + gender + "','" + address + "','" + contact + "','" + email + "','" + password + "')"
        ref.execute(query)
        con.commit()
    except Exception as err:
        errorWrite(str(err).capitalize(), "Customer_Table")
    finally:
        con.close()


def insertDriverData(address, contact, email, gender, licence, name, password, status):
    con = sql.connect("ProjectDatabase.db")
    try:
        ref = con.cursor()
        ref.execute(
            'CREATE TABLE IF NOT EXISTS Drivers(DId INTEGER PRIMARY KEY AUTOINCREMENT,DName Varchar(30),'
            'DGender char(6) ,DAdd varchar(40),DContact char(10),'
            'DEmail varchar(30),DPassword varchar(20),DStatus char(3),DLicenceNo char(10))')
        query = "INSERT INTO Drivers (DName,DGender,DAdd,DContact,DEmail,DPassword,DStatus,DLicenceNo) VALUES ('" + name + "','" + gender + "','" + address + "','" + contact + "','" + email + "','" + password + "','" + status + "','" + licence + "')"
        ref.execute(query)
        con.commit()
    except Exception as err:
        errorWrite(err, "Driver_Table  ")
    finally:
        con.close()


def checkCustomerData(email):
    con = sql.connect("ProjectDatabase.db")
    data = ()
    try:
        ref = con.cursor()
        query = "SELECT CEmail,CPassword FROM Customers WHERE CEmail = '{}'".format(email)
        temp = list(ref.execute(query))
        data = temp[0] if len(temp) else ()
        con.commit()
    except Exception as err:
        errorWrite(str(err).capitalize(), "Customer_Table")
    finally:
        con.close()
        return data


def checkDriverData(email):
    con = sql.connect("ProjectDatabase.db")
    data = ()
    try:
        ref = con.cursor()
        query = "SELECT DEmail,DPassword FROM Drivers WHERE DEmail = '{}'".format(email)
        temp = list(ref.execute(query))
        data = temp[0] if len(temp) else ()
        con.commit()
    except Exception as err:
        errorWrite(str(err).capitalize(), "Driver_Table  ")
    finally:
        con.close()
        return data
