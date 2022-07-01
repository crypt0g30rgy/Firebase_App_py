import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth=firebase.auth()

email=input("provide Your Sign in email: ")
password=input("provide Your Password: ")

try:
  auth.sign_in_with_email_and_password(email, password)
  print("Signed In. ")

except:
  print("Bad Email or Password. ")

email=input("provide Your email: ")
password=input("provide Your Password: ")
Pass_Confirm=input("Confirm Your Password: ")
try:
  if password==Pass_Confirm
  auth.create_user_with_email_and_password(email, password)
  print("Account created")

except:
  print("Account with given email already exists. ")

