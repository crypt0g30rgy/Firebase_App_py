import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

storage=firebase.storage()

#Upload file
localfile=input("Enter Filename you want to upload: ")
cloudfile_up=input("Enter Filename and path you want to upload as: ")

storage.child(cloudfile_up).put(localfile)

print("File upload SUCCESS; preview url: "+ storage.child(cloudfile_up).get_url(None))

#Download File
cloudfile_down=input("Enter path of/and Filename you want to downloadload: ")
localfile=input("enter filename you want to save as: ")

storage.child(cloudfile_down).download(localfile)

#Stream uploaded File 
cloudfile=input("enter filename you want to check: ")

stream_url=storage.child(cloudfile).get_url(None)

stream_url=urllib.requests.urlopen(url).read()

print(stream_url)

