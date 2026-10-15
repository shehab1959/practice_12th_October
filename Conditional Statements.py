user_age = int(input("Enter your age: "))
print(user_age)

if user_age >= 18 : #(if True/False) ->We can also use this
    print("You're Adult")
else :
    print("You're NOT Adult")


##
roll_no = int(input("Enter your roll here: "))

if roll_no == 1098 :
    print("Pass")
else :
    print("Fail")


##
user_age = int(input("Enter your age: "))
print(user_age)

if user_age < 18 : 
    print("Junior")
elif 18 <= user_age <= 40 :                  #Evebe likha jay condition
    print("Young Blood")
elif (user_age > 40) and (user_age <=60) :   #Or Evabe o likha jay
    print("Mid Age")
else :
    print("Senior Citizen")


##
user_age = int(input("Enter your age: "))
print(user_age)

if user_age >= 18 :
    print("You're eligible for driving linance")
else :
    print("You're NOT eligible")
