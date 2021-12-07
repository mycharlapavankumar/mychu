import numpy as np
import cv2
import pickle

face_cascade=cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels ={"person_name":1}
with open("lables.pickle", 'rb') as f:
    or_labels= pickle.load(f)
    labels ={v:k for k,v in or_labels.items()}

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    for (x,y,w,h) in faces:
       # print(x,y,w,h)
        roi_gray=gray[y:y+h ,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        id_,conf=recognizer.predict(roi_gray)
        if conf>=45 and conf<=85:
            print(id_)
            print(labels[id_])
            font= cv2.FONT_HERSHEY_SIMPLEX
            name= labels[id_]
            color=(255.255,255)
            stroke=3
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            
        img_item = "my_img.png"
        cv2.imwrite(img_item,roi_gray)
        color =(0,0,255)
        stroke=2
        width=x+w
        height=y+h
        cv2.rectangle(frame,(x,y),(width,height),color,stroke)

    cv2.imshow('video',frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

cap.release()


