'''import csv
fieldnames=['Id','Name']
with open ("details.csv") as f:
    thewriter =csv.DictWriter(f,fieldnames=fieldnames)
    csv_r=csv.reader(f)
    for i in csv_r:
        print(i)
        df = pd.read_csv("details.csv")
    
'''
import pandas as pd
import csv 

pf=pd.read_csv('Attendance_1234.csv')
print(pf)
    
