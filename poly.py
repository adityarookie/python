class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("meow")

    def info(self):
        print("i am a cat my name is",self.name,"I am",self.age,"years old")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("bark")

    def info(self):
        print("i am a dog my name is",self.name,"I am",self.age,"years old")    
 
cat1 = cat("chinchin",11)
dog1 = dog("puppy",7)

for i in(cat1,dog1):
    i.info()
    i.make_sound()