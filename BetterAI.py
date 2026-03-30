print("I am AI bot.What can i do for you today? :)")
name = input("What is your name?")

print("nice to meet you",name)
print("How are you feeling",name,"?")

mood = input().lower()

if mood == "good":
    print("im glad to hear that!")
elif mood =="bad":
    print("im sorry to hear that :(")
else:
    print("I see.Sometimes its hard to put into words what you are feeling")

print("if you dont mind me asking? How old are you",name)

age = int(input())
if age<5:
    print("what are you doing here? You are still a kid :)")
elif age<10:
    print("you are quite young")
elif age<20:
    print("You are a teenager arent you?")
else: 
    print("you are too old to be using this Chatbot :)")

print("It was nice chatting with you",name,"hope to see your again.")
