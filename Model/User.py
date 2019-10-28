import Controller.CrudController
import json
import fileinput


class User:
    def __init__(self):
        self.CRUD = Controller.CrudController.CRUD("User.txt")

    def getUsers(self):
        users=[]
        data = self.CRUD.readAll().split('\n')
        for i in data:
            parse = json.loads(i)
            users.append(UserModel(parse['id'],parse['name'],parse['age']))
        return users

    def addUser(self,name,age):
        last = self.getUsers()
        buff = '{ "id":'+str(last[-1].id+1)+',"name":"'+name+'","age":'+str(age)+' }'
        self.CRUD.Write(buff)

    def findRecord(self, col, value):
        data = self.CRUD.readAll().split('\n')
        pos =0
        for i in data:
            parsed = json.loads(i)
            if parsed[col] == value:
                return pos
            pos+=1

    def update(self,col,val,colu,vals):
        raw = self.CRUD.readAll()
        rw = raw.split('\n')
        row = self.findRecord(col,val)
        data = json.loads(rw[row])
        a = str(rw[row])
        old = '"'+colu+'":"'+str(data[colu])+'"'
        new = '"'+colu+'":"'+str(vals)+'"'
        a = a.replace(old,new)
        raw= raw.replace(old,new)
        self.CRUD.forceWrite(raw)


            

class UserModel:
    def __init__(self,id, name,age):
        self.id = id
        self.name=name
        self.age = age
