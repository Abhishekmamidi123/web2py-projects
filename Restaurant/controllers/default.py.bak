# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    Rest_names=db().select(db.Restaurant.ALL,orderby=db.Restaurant.Restaurant_Name)
#    for iterator in Rest_names :
    return dict(Rest_names = Rest_names)
    #return dict(Rest_names=Rest_names)
#    response.flash = T("Hello World")
    #return dict(message=T('Welcome to web2py!'))
def Menu_Item():
    Rest = request.args(0)
    rest = db(db.Restaurant.Restaurant_Name == request.args(0)).select()
    rowes = db(db.Menu.Restaurant_Name == request.args(0)).select()
    return locals()

def register():
    Register = SQLFORM.factory(Field('Restaurant',unique = True,requires = IS_NOT_EMPTY()),
                               Field('Contact_Number',unique = True,requires = IS_INT_IN_RANGE(minimum = 1000000000,maximum = 9999999999)),
                               Field('Address','text',requires = IS_NOT_EMPTY()),
                               Field('Open_Time','time',requires = IS_NOT_EMPTY()),
                               Field('Close_Time','time', requires = IS_NOT_EMPTY()),
                               Field('Login_Name',requires = IS_NOT_EMPTY()),
                               Field('Password','password',requires = IS_NOT_EMPTY())).process()

    if Register.accepted :
        try :
            db.Restaurant.insert(Restaurant_Name = Register.vars.Restaurant,
                             Mobile_Number = Register.vars.Contact_Number,
                             Address = Register.vars.Address,
                             Open_Time = Register.vars.Open_Time,
                             Close_Time = Register.vars.Close_Time,
                             Login_Name = Register.vars.Login_Name,
                             Password = Register.vars.Password)
            redirect(URL("index"))
        except :
            response.flash = "User already exists"
    elif Register.errors:
        response.flash = "Fill all details"
    else :
        response.flash = "First time"
    return dict(Register = Register)

def deregister() :
    Deregister = SQLFORM.factory(Field('Restaurant',unique = True,requires = IS_NOT_EMPTY()),
                               Field('Password','password',requires = IS_NOT_EMPTY()))
    item_names = db().select(db.Menu.ALL)
    Rests = db().select(db.Restaurant.ALL)
    flag = 0
    if Deregister.process().accepted :
        for iterator in Rests :
            if Deregister.vars.Restaurant == iterator.Restaurant_Name :
                if Deregister.vars.Password == iterator.Password :
                    flag = 1
                    break
        if flag == 1 :
            for iterator in item_names :
                if Deregister.vars.Restaurant == iterator.Restaurant_Name :
                    db(db.Menu.Restaurant_Name == Deregister.vars.Restaurant).delete()
            for iterator in Rests :
                if Deregister.vars.Restaurant == iterator.Restaurant_Name :
                    db(db.Restaurant.Restaurant_Name == Deregister.vars.Restaurant).delete()
            response.flash = "Deregistered Successfully"
            Rests = db().select(db.Restaurant.ALL)
        else :
            response.flash = "Password incorrect"
            redirect(URL("deregister"))
        return dict(Deregister = Deregister,Rests=Rests)
    return locals()

#@auth.requires_login()
def login() :
    Rest = request.vars.Rest
    Login = SQLFORM.factory(Field('Restaurant',unique = True,requires = IS_NOT_EMPTY()),
                               Field('Password','password',requires = IS_NOT_EMPTY()))
    Rests = db().select(db.Restaurant.ALL)
    flag = 0
    if Login.process().accepted :
        for iterator in Rests :
            if Login.vars.Restaurant == iterator.Restaurant_Name :
                if Login.vars.Password == iterator.Password :
                    flag = 1
                    Rest = iterator.Restaurant_Name
                    break

    if flag == 1 :
        redirect(URL("menu",args=[Rest]))
        return dict(Login = Login,Rest = Rest)
    else :
        return dict(Login = Login,Rest = Rest)
        response.flash('Login Failed')

def menu() :
    Rest = request.args
    #response.flash = T("Hello World")
    #return dict(message=Rest)
    return locals()

def Add_Item() :
    Rest=request.args
    Add = SQLFORM.factory(Field('Item_name',unique = True,requires = IS_NOT_EMPTY()),
                          Field('Price_in_Rs',requires = IS_NOT_EMPTY()))
    if Add.process().accepted :
        db.Menu.insert(Restaurant_Name=Rest[0] , Item_Name=Add.vars.Item_name , Price=Add.vars.Price_in_Rs)
#        redirect(URL("menu/{{=Rest[0]}}"))
#    return Rest
    return dict(Add=Add,Rest=Rest)

def Edit_Item() :
    Rest=request.args
    flag = 0
    Edit = SQLFORM.factory(Field('Item_name',unique = True,requires = IS_NOT_EMPTY()),Field('Price_in_Rs',unique = True,requires = IS_NOT_EMPTY()))
    item_names = db().select(db.Menu.ALL,orderby = db.Menu.Item_Name)
    if Edit.process().accepted :
        for iterator in item_names :
            if Edit.vars.Item_name == iterator.Item_Name and iterator.Restaurant_Name == Rest[0] :
                db(db.Menu.Item_Name == Edit.vars.Item_name).update(Price = Edit.vars.Price_in_Rs)
                flag = 1
                break
#                redirect(URL("menu"))
        if flag!=1 :
            response.flash = "Can't find your item"
            flag = 0
    return dict(Edit = Edit,Rest=Rest)

def Delete_Item() :
    Rest=request.args
    flag = 0
    Delete = SQLFORM.factory(Field('Item_name',unique = True,requires = IS_NOT_EMPTY()))
    item_names = db().select(db.Menu.ALL,orderby = db.Menu.Item_Name)
    if Delete.process().accepted :
        for iterator in item_names :
            if Delete.vars.Item_name == iterator.Item_Name and iterator.Restaurant_Name == Rest[0] :
                response.flash = "Deleted successfully"
                db(db.Menu.Item_Name == Delete.vars.Item_name).delete()
                flag = 1
#                redirect(URL("menu"))
        if flag!=1 :
            response.flash = "Can't find your item"
            flag = 0
    return dict(Delete = Delete,Rest=Rest)

def show() :
    post = db.Restaurant(request.args(0,cast = int))
    return locals()

def SelectByTime() :
    Time = SQLFORM.factory(Field('Time','time',requires = IS_NOT_EMPTY()))
    abhi = db(db.Restaurant).select()
    if Time.process().accepted :
        abhi = db((db.Restaurant.Open_Time<=Time.vars.Time) & (db.Restaurant.Close_Time>=Time.vars.Time)).select()
        return locals()
    return locals()
