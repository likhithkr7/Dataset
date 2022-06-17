# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
from random import randint
from random import sample
import pandas as pd 

# ID,Object,SensorID,Sensors,Sensor_values,Sensor_status,Location,X,Y,Activity
# Kitchen

Dataset = []

Objects = ['stove','hotplate','oven','utensil']

Sensor_values = {"Temperature": [-55, 126],
        "Pressure": [10, 51],
        "Force": [0, 51],
        "Light": [1, 40000],
        "IR": [2, 10],
        "Noise": [20, 20000],
        "Motion_Detection": [25, 2000],
        "Pulse": [60, 100],
        "Humidity": [-30, 190],
        "Magnetic": [0, 20],
        "Accelerometer": [1, 250],
        "IR Proximity": [10, 80],
        "Ultrasonic": [40, 70000],
        "Level": [0, 4]}

Sensors = {"stove": [ "Temperature", "Motion_Detection"],
    "hotplate" : [ "Temperature", "Motion_Detection"],
    "oven": [ "Temperature", "Motion_Detection"],
    "utensil": [  "Temperature", "Motion_Detection"],
    "tv": [  "Light", "Noise"],
    "chair": [  "Motion_Detection", "Pressure", "Force"],
    "book": [ "IR Proximity", "Force", "Noise"],
    "mobile": [ "Temperature","Force", "Light", "Motion_Detection", "IR Proximity"],
    "bed": [ "Pressure", "Force"],
    "wardrobe": [  "Force", "Motion_Detection", "IR Proximity"],
    "Bathroom door": [  "IR Proximity", "Noise", "Force"],
    "Water closet": [  "IR Proximity", "Pressure", "Noise"],
    "Shower cabinet": [  "IR Proximity", "Noise", "Temperature", "Level"]}

Activity = ['Preparing food', 'Having food', 'Washing Dishes']

loc_set = set()

def x_y(loc):
    x = randint(50,480)
    y = randint(40,280)
    z = str(x)+"_"+str(y)+"_"+loc
    s = str(hash(z))
    if s not in loc_set:
        loc_set.add(s)
        return [x,y]
    return x_y(loc)
    
    

for ID in range(0,25001):
    row=[]
    row.append(ID)
    obj = random.choice(tuple(Objects))
    row.append(obj)
    N_no_sen = randint(1,len(Sensors[obj]))
    N_sen = sample(Sensors[obj],N_no_sen)
    N_sen_val = []
    N_sen_st = []
    for x in N_sen:
        val = randint(Sensor_values[x][0],Sensor_values[x][1])
        N_sen_val.append(str(val))
        mid = (Sensor_values[x][0]+Sensor_values[x][1])/2
        if(val<mid):
            N_sen_st.append("low")
        else:
            N_sen_st.append("high")
    str1=""
    S = ""
    V = ""
    ST = ""
    for i in range(0,len(N_sen)):
        str1+=N_sen[i]
        if(N_sen_st[i]=="low"):
            str1+="l"
        else:
            str1+="h"
        S += N_sen[i]
        V += N_sen_val[i]
        ST += N_sen_st[i]
        if(i!=len(N_sen)-1):
            S+=","
            V+=","
            ST+=","
    Group_sen_id = hash(str1)
    row.append(Group_sen_id)
    row.append(S)
    row.append(V)
    row.append(ST)
    row.append("Kitchen")
    l = x_y("Kitchen")
    x = l[0]
    y = l[1]
    row.append(x)
    row.append(y)
    A = sample(Activity,1)
    row.append(A[0])
    Dataset.append(row)
    

#Living_Room

Objects = ["tv","chair","book"]

Activity = ["Going Out", "Watching TV", "Studying", "Reading Book", "Talking on the phone"]

for ID in range(25001,50001):
    row=[]
    row.append(ID)
    obj = random.choice(tuple(Objects))
    row.append(obj)
    N_no_sen = randint(1,len(Sensors[obj]))
    N_sen = sample(Sensors[obj],N_no_sen)
    N_sen_val = []
    N_sen_st = []
    for x in N_sen:
        val = randint(Sensor_values[x][0],Sensor_values[x][1])
        N_sen_val.append(str(val))
        mid = (Sensor_values[x][0]+Sensor_values[x][1])/2
        if(val<mid):
            N_sen_st.append("low")
        else:
            N_sen_st.append("high")
    str1=""
    S = ""
    V = ""
    ST = ""
    for i in range(0,len(N_sen)):
        str1+=N_sen[i]
        if(N_sen_st[i]=="low"):
            str1+="l"
        else:
            str1+="h"
        S += N_sen[i]
        V += N_sen_val[i]
        ST += N_sen_st[i]
        if(i!=len(N_sen)-1):
            S+=","
            V+=","
            ST+=","
    Group_sen_id = hash(str1)
    row.append(Group_sen_id)
    row.append(S)
    row.append(V)
    row.append(ST)
    row.append("Living_Room")
    l = x_y("Living_Room")
    x = l[0]
    y = l[1]
    row.append(x)
    row.append(y)
    A = sample(Activity,1)
    row.append(A[0])
    Dataset.append(row)
    
#Bedroom

Objects = [ "mobile","book","bed","tv", "wardrobe"]

Activity = ["Sleeping", "Watching TV", "Studying", "Reading Book", "Talking on the phone"]

for ID in range(50001,75001):
    row=[]
    row.append(ID)
    obj = random.choice(tuple(Objects))
    row.append(obj)
    N_no_sen = randint(1,len(Sensors[obj]))
    N_sen = sample(Sensors[obj],N_no_sen)
    N_sen_val = []
    N_sen_st = []
    for x in N_sen:
        val = randint(Sensor_values[x][0],Sensor_values[x][1])
        N_sen_val.append(str(val))
        mid = (Sensor_values[x][0]+Sensor_values[x][1])/2
        if(val<mid):
            N_sen_st.append("low")
        else:
            N_sen_st.append("high")
    str1=""
    S = ""
    V = ""
    ST = ""
    for i in range(0,len(N_sen)):
        str1+=N_sen[i]
        if(N_sen_st[i]=="low"):
            str1+="l"
        else:
            str1+="h"
        S += N_sen[i]
        V += N_sen_val[i]
        ST += N_sen_st[i]
        if(i!=len(N_sen)-1):
            S+=","
            V+=","
            ST+=","
    Group_sen_id = hash(str1)
    row.append(Group_sen_id)
    row.append(S)
    row.append(V)
    row.append(ST)
    row.append("Bedroom")
    l = x_y("Bedroom")
    x = l[0]
    y = l[1]
    row.append(x)
    row.append(y)
    A = sample(Activity,1)
    row.append(A[0])
    Dataset.append(row)
    
#Bathroom

Objects = ["Bathroom door", "Water closet", "Shower cabinet"]

Activity = ["Having Shower", "Toileting", "Laundry", "Brushing Teeth", "Shaving", "Cleaning"]

for ID in range(75001,100001):
    row=[]
    row.append(ID)
    obj = random.choice(tuple(Objects))
    row.append(obj)
    N_no_sen = randint(1,len(Sensors[obj]))
    N_sen = sample(Sensors[obj],N_no_sen)
    N_sen_val = []
    N_sen_st = []
    for x in N_sen:
        val = randint(Sensor_values[x][0],Sensor_values[x][1])
        N_sen_val.append(str(val))
        mid = (Sensor_values[x][0]+Sensor_values[x][1])/2
        if(val<mid):
            N_sen_st.append("low")
        else:
            N_sen_st.append("high")
    str1=""
    S = ""
    V = ""
    ST = ""
    for i in range(0,len(N_sen)):
        str1+=N_sen[i]
        if(N_sen_st[i]=="low"):
            str1+="l"
        else:
            str1+="h"
        S += N_sen[i]
        V += N_sen_val[i]
        ST += N_sen_st[i]
        if(i!=len(N_sen)-1):
            S+=","
            V+=","
            ST+=","
    Group_sen_id = hash(str1)
    row.append(Group_sen_id)
    row.append(S)
    row.append(V)
    row.append(ST)
    row.append("Bathroom")
    l = x_y("Bathroom")
    x = l[0]
    y = l[1]
    row.append(x)
    row.append(y)
    A = sample(Activity,1)
    row.append(A[0])
    Dataset.append(row)

df = pd.DataFrame(Dataset, columns =["ID","Object","SensorID","Sensors","Sensor_values","Sensor_status","Location","X","Y","Activity"], dtype = int)
print(df)

df.to_csv('Dataset.csv')

