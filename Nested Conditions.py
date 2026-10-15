age = int(input("Enter your age: "))
print(type(age))
has_licence = False

if age >= 18 :
    if has_licence:
        print ("You are eligible for driving")
    else :
        print("Get a driving license first")
else :
    print("You are not eligible, get 18 first")



###
age1 = 18
has_license = False

if age1 >= 18:
    if has_license:
        print("You can drive cars")
    else:
        print("You need a license to drive cars")
else:
    print("You are too young too drive!")



###
temperature = int(input("Enter today's Temparature: "))
is_sunny = True

if temperature > 15:
    print("The weather is warm enough. Let's go out.")
else:
    if is_sunny:
        print("It's cold, but sunny. Let's go out.")
    else:
        print("It's cold and not sunny, so it's risky to go outside.")