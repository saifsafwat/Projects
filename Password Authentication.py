
import getpass
database = {"aman.kharwal":"123456","kharwal.aman":"654321"}
username= input("Enter your Username : ")
password = getpass.getpass("Enter your Password : ")
for i in database.keys() :
    if username ==i :
        while password != database.get(i) :
            password =getpass.getpass("Enter Your Password Again: ")
            break
        print ("verified")