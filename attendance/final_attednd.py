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
import imutils
import math


bg = None



df = pd.read_csv("Details\details.csv")
df.to_csv("Attendance\Attendance_1234.csv",index=False)



window = tk.Tk()

window.title("Face recongeier")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text="Are you sure?"
window.configure(background='blue')
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0, weight=1)

message =tk.Label(window, text ="Dept of ECE ANITS smart attendance system",bg="blue",fg="white",width=50,height=3,font=('times',30,'italic bold underline'))
message.place(x=100,y=20)

lb1=tk.Label(window, text ="Enter ID", width=20, height =2, fg="red" , bg="yellow",font=('time',15,'bold'))
lb1.place(x=200,y=200)
txt=tk.Entry(window,width=20,bg="pink",fg=  "red",font=('times',25,'bold'))
txt.place(x=550,y=210)
lb2=tk.Label(window, text ="Enter Name", width=20, height =2, fg="red" , bg="yellow",font=('time',15,'bold'))
lb2.place(x=200,y=300)
txt2=tk.Entry(window,width=20,bg="pink",fg=  "red",font=('times',25,'bold'))
txt2.place(x=550,y=310)

lb3=tk.Label(window, text ="Notification", width=20, height =2, fg="red" , bg="yellow",font=('time',15,'bold'))
lb3.place(x=200,y=400)
message =tk.Label(window, text ="",bg="pink",fg="red",width=30,height=2, activebackground="pink",font=('times',15,'italic bold underline'))
message.place(x=550,y=400)
lb3=tk.Label(window, text ="Attendance", width=20, height =2, fg="red" , bg="yellow",font=('time',15,'bold underline'))
lb3.place(x=200,y=620)
message2 =tk.Label(window, text ="",bg="pink",fg="red",width=30,height=2, activebackground="pink",font=('times',15,'italic bold underline'))
message2.place(x=550,y=620)

def clear():
    txt.delete(0,'end')
    reg=""
    message.configure(text=reg)
def clear2():
    txt2.delete(0,'end')
    reg=""
    message.configure(text=reg)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError :
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

    

def TakeImages():
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam=cv2.VideoCapture(0)
        harcascadePath = "cascade/data/haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret,img=cam.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=detector.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                sampleNum=sampleNum+1
                cv2.imwrite("TraniningImages\ "+name+"." + Id + '-' +str(sampleNum) + ".jpg" , gray[y:y+h,x:x+h])
                cv2.imshow('Frame',img)
            if cv2.waitKey(100) & 0x77 == ord('q'):
                break
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        reg="Image Saved for ID: " + Id + "Name :"+name
        row=[Id,name]
        with open('Details\details.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()                     
        message.configure(text=reg)
        
    else :
        if(is_number(Id)):
            reg ="Enter Alphabetical Name"
            message.configure(text =reg)
        if (name.isalpha()):
            reg="Enter numeric ID"
            message.configure(text=reg)


def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "cascade/data/haarcascade_frontalface_default.xml"
    detector=cv2.CascadeClassifier(harcascadePath)
    faces,Id=getImageAndLables("TraniningImages")
    recognizer.train(faces,np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res ="Image Trained"
    message.configure(text=res)

def getImageAndLables(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        pp=os.path.split(imagePath)[-1].split(".")[1][0]
        Id=int(pp)
        faces.append(imageNp)
        Ids.append(Id)  
    return faces,Ids


def TrackImages():
    cam=cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "cascade/data/haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("Details\details.csv")
    font=cv2.FONT_HERSHEY_SIMPLEX
    ts=time.time()
    date =datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
    pf=pd.read_csv('Attendance\Attendance_1234.csv',index_col=0)
    col_names=["Id","name","Date","Time"]
    attendance = pd.DataFrame(columns=col_names)
    pp=0
    while True:
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
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
                cv2.putText(img,str(tt),(x,y+h),font,1,(225,255,0),2)
                cv2.imshow('im',img)
                time.sleep(5)
                cam.release()
                check=hand()
                cam=cv2.VideoCapture(0)
                print(check)
                if check ==1:
                    
                    pf.loc[Id,date[:2]]=1
                    print(pf.loc[Id,date[:2]])
                    pf.loc[Id,'Name']=aa
                    attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    pp=50
            else:
                Id="Unkown"
                tt=str(Id)
                if(conf>75):
                    noOfFile=len(os.listdir("ImagesUnkown"))+1
                    cv2.imwrite("ImagesUnkown\Imagr"+str(noOfFile)+".jpg",img[y:y+h,x:x+w])
            cv2.putText(img,str(tt),(x,y+h),font,1,(225,255,0),2)
            attendance = attendance.drop_duplicates(subset=['Id'],keep='first')
            cv2.imshow('im',img)
            pp+=1
            
        
        ts=time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M,%S')
        hour,Min=timeStamp.split(":")
        Min,sec=Min.split(",")
            
            
        fileName="Attendance\Attendance_"+date+".csv"
            #attendance.to_csv(fileName,index=True)
        pf.to_csv(fileName)
        
        pf.to_csv("Attendance\Attendance_1234.csv")
        if( pp>=50 or cv2.waitKey(100)==ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    message2.configure(text=res)


def segment(image, threshold=25):
    global bg
    # find the absolute difference between background and current frame
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

    # get the contours in the thresholded image
    (cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # return None, if no contours detected
    if len(cnts) == 0:
        return
    else:
        # based on contour area, get the maximum contour which is the hand
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented,cnts)
        
def run_avg(image, aWeight):
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, bg, aWeight)

def hand():
     # initialize weight for running average
    aWeight = 0.5
    att=0

    # get the reference to the webcam
    camera = cv2.VideoCapture(0)

    # region of interest (ROI) coordinates
    top, right, bottom, left = 50, 400, 350, 650

    # initialize num of frames
    num_frames = 0
    count=0

    # keep looping, until interrupted
    while(True):
        # get the current frame
        (grabbed, frame) = camera.read()

        # resize the frame
        frame = imutils.resize(frame, width=700)

        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)
        

        # clone the frame
        clone = frame.copy()
        

        # get the height and width of the frame
        (height, width) = frame.shape[:2]

        # get the ROI
        roi = frame[top:bottom, right:left]
        

        # convert the roi to grayscale and blur it
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
       
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
       

        # to get the background, keep looking till a threshold is reached
        # so that our running average model gets calibrated
        if num_frames < 30:
            run_avg(gray, aWeight)
        else:
            # segment the hand region
            hand = segment(gray)

            # check whether hand region is segmented
            if hand is not None:
                # if yes, unpack the thresholded image and
                # segmented region
                (thresholded, segmented,contours) = hand

                # draw the segmented region and display the frame
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                cv2.imshow("Thesholded", thresholded)

                try:
                    contour = max(contours,key=lambda x:cv2.contourArea(x))
                    x,y,w,h=cv2.boundingRect(contour)
                    cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),0)
                    hull=cv2.convexHull(contour)
                    drawing=np.zeros(roi.shape,np.uint8)
                    cv2.drawContours(drawing,[contour],-1,(0,255,0),0)
                    cv2.drawContours(drawing,[hull],-1,(0,0,255),0)
                    hull=cv2.convexHull(contour,returnPoints=False)
                    defects=cv2.convexityDefects(contour,hull)
                    count_defects=0
                    
                    for i in range(defects.shape[0]):
                        s,e,f,d=defects[i,0]
                        start=tuple(contour[s][0])
                        end=tuple(contour[e][0])
                        far=tuple(contour[f][0])

                        a=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
                        b=math.sqrt((far[0]-start[0])**2+(far[1]-start[1])**2)
                        c=math.sqrt((end[0]-far[0])**2+(end[1]-far[1])**2)
                        angle=(math.acos((b**2+c**2-a**2)/(2*b*c))*180)/3.14
                        if angle<=90:
                            count_defects+=1
                            cv2.circle(roi,far,1,[0,0,255],-1)
                            cv2.line(roi,start,end,[0,255,0],2)
                   
                    if count_defects==3 or count_defects==4:
                        count+=1
                        cv2.putText(clone,"ok ",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
                    else:
                        cv2.putText(clone,"show ok ",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
                        
                except:
                    pass
                        

                    
                    

        # draw the segmented hand
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)

        # increment the number of frames
        num_frames += 1

        # display the frame with segmented hand
        cv2.imshow("Video Feed", clone)
        if count == 50:
            att=1

        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF

        # if the user pressed "q", then stop looping
        if keypress == ord("q") or  att==1:
            camera.release()
            cv2.destroyAllWindows()
            break
    return att
    # free up memory
    
    

    
    
            

clearButton =tk.Button(window,text='clear', command=clear,fg='red',bg="green" ,width=20,activebackground="Red",font=('times',15,'bold'))
clearButton.place(x=930,y=210)

clearButton2 =tk.Button(window,text='clear', command=clear2,fg='red',bg="green" ,width=20,activebackground="Red",font=('times',15,'bold'))
clearButton2.place(x=930,y=310)
takeImg=tk.Button(window,text="Taken Image", command=TakeImages,fg="red",bg="green",width=20,height=3,activebackground="RED",font=('time',15,'bold'))
takeImg.place(x=90,y=500)
trainImg=tk.Button(window,text="Train Image", command=TrainImages,fg="red",bg="green",width=20,height=3,activebackground="RED",font=('time',15,'bold'))
trainImg.place(x=390,y=500)

trackImg=tk.Button(window,text="track Image", command=TrackImages,fg="red",bg="green",width=20,height=3,activebackground="RED",font=('time',15,'bold'))
trackImg.place(x=690,y=500)

quitWindow=tk.Button(window,text="quit", command=window.destroy,fg="red",bg="green",width=20,height=3,activebackground="RED",font=('time',15,'bold'))
quitWindow.place(x=990,y=500)

