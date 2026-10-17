count = 0

while count < 5 :
    print("Hejbulla Asad Shehab")
    count = count + 1
print("finish")

##
count1 = 3
while count1 > 0 :
    print("DIU")
    count1 = count1 - 1








##GAME using while loop

save_in_computer = 3

while True: #Bar bar loop cholte thakar jnno right guess na pawa prjnto
    user_input = int(input("Enter a random number: "))

    if user_input == save_in_computer :
        print("Right guess")
        break
    else :
        print("Wrong, Try Again!")


##For Randomly number save in computer, Not manually set
import random
save_in_computer = random.randint(1,10)


while True: #Bar bar loop cholte thakar jnno right guess na pawa prjnto
    user_input = int(input("Enter a random number: "))

    if user_input == save_in_computer :
        print("Right guess")
        break
    else :
        print("Wrong, Try Again!")


#End of this cls