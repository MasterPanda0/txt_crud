import Model.User


tester = Model.User.User()

data = tester.getUsers()
for i in data:
    print(i.id,i.name,i.age)
tester.update('name','budi','age',"88")
