import cv2
import face_recognition
import pickle
import os
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
#
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred,{
# 'databaseURL':"https://facerecognition-bb913-default-rtdb.firebaseio.com/",
#     'storageBucket':"facerecognition-bb913.appspot.com"
# })

folderPath = 'Images'

PathList = os.listdir(folderPath)

imgList=[]
personId = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    personId.append(os.path.splitext(path)[0])
    # fileName = f'{folderPath}/{path}'
    #
    # buckets = storage.bucket()
    # blob = buckets.blob(fileName)
    # blob.upload_from_filename(fileName)

print(personId)

def findEncoding(imgList):
    encodeList=[]
    for img in imgList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncoding(imgList)
encodeListKnownwithID = [encodeListKnown,personId]
print(encodeListKnown)
print("Encoding complete")

file = open("Encodefile.p",'wb')
pickle.dump(encodeListKnownwithID,file)
file.close()
print("File Saved")