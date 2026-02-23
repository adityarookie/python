class robot:
    def __init__(self,name):
       self.name = "TOM"
       
    def introduce(self):
        print("hello my name is",self.name)


robot1 = robot("tom")
robot2 = robot("jerry")

robot1.introduce()
robot2.introduce()

