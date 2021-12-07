import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"faces")
face_cascade=cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

y_label=[]
x_train=[]
current_id=1
label_ids ={}


for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jfif") or file.endswith("jpeg") :
            path=os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label,path)
           
            if not label in label_ids:
                label_ids[label]=current_id
                current_id +=1
            id_=label_ids[label]
            print(label_ids)
            pil_image=Image.open(path).convert("L")
            image_array=np.array(pil_image,"uint8")
            #print(image_array)
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.3,minNeighbors=5)
            for (x,y,w,h) in faces:
                roi= image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_label.append(id_)



with open("lables.pickle", 'wb') as f:
    pickle.dump(label_ids,f)


recognizer.train(x_train,np.array(y_label))
recognizer.save("trainner.yml")
