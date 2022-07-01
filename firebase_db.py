import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#Print the whole DB
print(db.get())

#Create a new single DB entry
DoB = input("enter birth day seperated by slashes: ")
first_Name = input("enter first name: ")
last_Name = input("enter last name: ")
Passphrase = input("enter a uniques passphrase: ")

data =  " ".join([DoB, first_Name, last_Name])

db.child("Accounts").push(data)

print("Account Data Uploaded Successfully. ")

#Update a single DB entry
DoB = input("enter birth day seperated by slashes: ")
first_Name = input("enter first name: ")
last_Name = input("enter last name: ")

update_data =  " ".join([DoB, first_Name, last_Name])

Accounts = db.child("Accounts").get()
for user in Accounts.each():
  if user.val()['passphrase']==input("enter passprase: "):
    print("details Updated Successfully. ")
 
db.child("Accounts").child(user.key()).update(update_data)

print("Account Data Updated Successfully. ")

#Delete data
Accounts = db.child("Accounts").get()
for user in Accounts.each():
  if user.val()['passphrase']==input("enter passprase: "):
    print("details deleted successfully. ")

db.child("Accounts").child(user.key()).remove()

