days_on = int(input("put in how many days you went to school "))
days_off = int(input("put in how many days your were absent "))
total = days_on + days_off

if days_on > 0 and days_off > 0  :
   if days_on / total >= 0.75 :
           print("you are eligible to take the exam")
   else:
       print("you need to attend school more!")
else:
  print("invalid conclusion")




