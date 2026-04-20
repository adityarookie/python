file = open("hello.txt","r")
print(file.read())
file.close()

file =open("hello.txt","a")
file.write("hello today we are going to be learning about science.")

file = open("hello.txt","r")
print(file.read())
file.close()