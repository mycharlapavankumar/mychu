import tkinter as tk
from tkinter import Message,Text
import cv2, os
import shutil
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
cam=cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("TrainingImageLabel\Trainner.yml")
harcascadePath = "cascade/data/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(harcascadePath)
df = pd.read_csv("Details\details.csv")
font=cv2.FONT_HERSHEY_SIMPLEX
ts=time.time()
date =datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
pf=pd.read_csv('Attendance\Attendancetest.csv')
col_names=["Id","name","Date","Time"]
attendance = pd.DataFrame(columns=col_names)
pp=0
while True:
        pp+=1
        print(pp)
        ret,img=cam.read()
        cv2.imshow('test',img)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print(gray,gray.shape)
        faces=detector.detectMultiScale(gray,1.2,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
            if (conf<50):
                ts=time.time()
                date=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M,%S')
                aa = df.loc[df['Id']==Id]['Name'].values
                #aa=pf[1]
                tt=str(Id)+"-"+aa
                print(pf)
                pf.loc[Id,date[:2]]=1
                print(type(date))
                
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
            else:
                Id="Unkown"
                tt=str(Id)
                if(conf>75):
                    noOfFile=len(os.listdir("ImagesUnkown"))+1
                    cv2.imwrite("ImagesUnkown\Imagr"+str(noOfFile)+".jpg",img[y:y+h,x:x+w])
            cv2.putText(img,str(tt),(x,y+h),font,1,(225,255,0),2)
            attendance = attendance.drop_duplicates(subset=['Id'],keep='first')
            cv2.imshow('im',img)
            if(cv2.waitKey(1)==ord('q')):
                break;
            ts=time.time()
            date =datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M,%S')
            hour,Min=timeStamp.split(":")
            Min,sec=Min.split(",")
            
            
            #fileName="Attendance\Attendance_"+date+".csv"
            #attendance.to_csv(fileName,index=True)
            pf.to_csv('Attendance\Attendancetest.csv',index=False)
            cv2.destroyAllWindows()
            res=attendance
           # message2.configure(text=res)
        
