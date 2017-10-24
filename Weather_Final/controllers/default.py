# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
def map() :
    return locals()
def temp() :
    response.flash = T("Hello World")
    info_update()
    read=db().select(db.Readings.ALL)
    return dict(read=read)
def index():
    response.flash = T("Hello World")
    info_update()
    read=db().select(db.Readings.ALL)
    TableNames = db().select(db.Arduino_Table.ALL,orderby = db.Arduino_Table.Place)
    db(db.Arduino_Table.id == 1).update(Temperature = 29.91)
    db(db.Arduino_Table.id ==1).update(Pressure    = 1234.56)
    db(db.Arduino_Table.id == 1).update(Humidity    = 43)
    return dict(read=read)

def find():
    import time
    date = []
    k = time.strftime("%d-%m-%Y")
    for i in range(4) :
        m = k
        a = m.split('-')
        z = str(int(a[0]) + i)
        a[0] = z
        date.append('-'.join(a))
    read =db().select(db.Readings.ALL)
    graph=db().select(db.Graph.ALL)
    s=request.vars.place
    rows=db(db.Graph.city==s).select()
    t=[]
    p=[]
    h=[]
    for i in rows:
        t.append(i.temperature)
        p.append(i.pressure)
        h.append(i.humidity)
    return dict(read=read,s=s,t=t,p=p,h=h,date=date)

def abhi() :
    TableNames = db().select(db.Arduino_Table.ALL,orderby = db.Arduino_Table.Place)
    return locals()

def temperature() :
    x=[];
    y=[];
    reading=db().select(db.Readings.ALL)
    for i in reading:
        x.append(i.place);
        y.append(int(i.low_temparature));
    #x=['a','b','d'];
    #y=[1,2,4];
    return dict(x=x,y=y,read=reading,reading=reading)
    #return locals()

def pressure() :
    x=[];
    y=[];
    reading=db().select(db.Readings.ALL)
    for i in reading:
        x.append(i.place);
        y.append(float(i.pressure));
    #x=['a','b','d'];
    #y=[1,2,4];
    return dict(x=x,y=y,read=reading,reading=reading)

def humidity() :
    x=[];
    y=[];
    reading=db().select(db.Readings.ALL)
    for i in reading:
        x.append(i.place);
        y.append(int(i.humidity));
    #x=['a','b','d'];
    #y=[1,2,4];
    return dict(x=x,y=y,read=reading,reading=reading)

def rainfall() :
    reading=db().select(db.Readings.ALL)
    return locals()

def imd_sensors() :
    reading=db().select(db.Readings.ALL)
    return dict(read=reading,reading=reading)

def iiit_sensors() :
    reading=db().select(db.Readings.ALL)
    return dict(read=reading,reading=reading)
def signup():
    a=request.args
    s="NULL"
    reading=db().select(db.Readings.ALL)
    if a[0]=="1":
        s="Sorry this Phone Number already exists!!"
    if a[0]=="2":
        s="Sorry this Email already exists!!"
    elif a[0]!="1" and a[0]!="2":
        s="gh "
    return dict(s=s,a=a[0],reading=reading,read=reading)

def signup1():
    flag=0
    a=request.vars.fname
    b=request.vars.phno
    c=request.vars.email
    d=request.vars.passwd
    su= db().select(db.Users.ALL)
    for i in su:
        if int(b)==i.phone_number:
            flag=1;
           
            redirect(URL('signup',args="1"))
            break;
            
        if c==i.email_id:
            flag=1;
          
            redirect(URL('signup',args="2"))
            break;
    if flag==0:
        db.Users.insert(name=a,phone_number=b,email_id=c,password=d)
      
        redirect(URL('index'))
        
def info_update() :
    import csv
    import os
    a = []
    with open('C:/Users/abhishek/Documents/Processing/weather/data/new.csv', 'r') as readfile:
        readcsv = csv.reader(readfile , delimiter = ',')
        print readcsv
        for row in readcsv :
            a.append(row)
        l = len(a)
        TableNames = db().select(db.Arduino_Table.ALL,orderby = db.Arduino_Table.Place)
        for iterator in TableNames :
            if "SRICITY" == iterator.Place :
                db(db.Arduino_Table.Place == "SRICITY").update(Temperature = a[l-1][7])
                db(db.Arduino_Table.Place == "SRICITY").update(Pressure    = a[l-1][8])
                db(db.Arduino_Table.Place == "SRICITY").update(Humidity    = a[l-1][9])
    TableNames = db().select(db.Arduino_Table.ALL,orderby = db.Arduino_Table.Place)
    return locals()


def graph() :
    x=[];
    y=[];
    a=0;
    id1=db().select(db.Readings.ALL)
    """for i in id1:
        x.append(i.place);
        y.append(int(i.low_temparature));
        a=1;"""
    x=['a','b','d'];
    y=[1,2,4];
    return dict(x=x,y=y)

def contactus():
    read=db().select(db.Readings.ALL)
    return dict(read=read)

def aboutus():
    read=db().select(db.Readings.ALL)
    return dict(read=read)

def t():
    return dict()
