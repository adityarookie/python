class person():
    def __init__(self,name,idnum):
        self.name = name
        self.idnum = idnum

    def display(self):
        print(self.name)
        print(self.idnum)

class employee(person):
    def __init__(self,salary,post,name,idnum):
        self.salary = salary
        self.post = post
        super().__init__(name,idnum)

obj = employee(100,"intern","Sahishnu",121)
obj.display()  
       