from msilib.schema import tables
from sys import stdin
import mysql.connector
import cv2
from cv2 import VideoCapture
from simple_facerec import SimpleFacerec
import time
import datetime as dt
import openpyxl as xl
import os


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="data_db"
)

nameincol = []
sfr = SimpleFacerec()
sfr.load_encoding_images('images/')
cap = cv2.VideoCapture(0)
process = True

mycursor = mydb.cursor()
sql = "INSERT INTO tb_students (name, studentid, classid, class, date, time, percent) values(%s, %s, %s, %s, %s, %s, %s)"
while True:
    
    ret, frame = cap.read()
    realtimedate = dt.datetime.now()
    date = str(realtimedate.strftime("%x"))
    time = str(realtimedate.strftime("%X"))
    
    face_locate = []
    
    
    if ret:
        face_locate, face_names, face_percent = sfr.detect_known_faces(frame)
        
        for (top,right,bottom,left), name in zip(face_locate, face_names):        
                
            onlyname = str(sfr.getNameFrom(name))
            classes = str(sfr.getClassesFrom(name))
            id = str(sfr.getNumberFrom(name))
            stdId = str(sfr.getStudentIdFrom(name))
            
            
            if name =='Unknown':
                onlyname = 'Unknown'
                classes = 'Unknown'
                id = 'Unknown'
            if onlyname not in nameincol and onlyname !='Unknown':
                nameincol.append(onlyname)
                val = (onlyname, stdId, id, classes, date, time, face_percent)
                mycursor.execute(sql,val)
                

                
                
                
                    
            
            if name == "Unknown":
                color = [46,2,209]
            else : 
                color = [255,102,45]              
            cv2.rectangle(frame, (left,top), (right,bottom), color, 4)
            cv2.rectangle(frame, (left-1, top-30), (right+1,top), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, onlyname, (left+6,top-6), font, 0.8, (255,255,255), 1)
            cv2.putText(frame, str(face_percent) + "%", (left+6,bottom+26), font, 0.6, (255,255,255), 1)
        
    
    cv2.imshow("FaceRecognition by M6/3", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

mydb.commit()