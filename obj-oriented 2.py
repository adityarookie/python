class fruit:
    def __init__(self):
        print("Employee is created")
    def __del__(self):
        print("called,destroyed")

obj = fruit()
print(obj)
del obj
print(obj)