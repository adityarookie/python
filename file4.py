with open("codingal.txt","w") as file:
    file.write("hello codingal i am here")

with open("codingal.txt","r") as file:
    x = file.readlines()
    print(x)
    print("\n")
    for lines in x:
        words = lines.split()

    print(words)
