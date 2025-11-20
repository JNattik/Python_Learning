#def my_function():
    #for i in range (1, 20):
        #if i == 20:
            #print("You got it.")

# my_function()
# Won't function, range function starts at 0 and goes till 19 not 20

#from random import randint
#dice_images = ["1", "2", "3", "4", "5", "6"]
#dice_num = randint(1, 6) #Won't work because the range is wrong --> must be 0, 5
#print(dice_images[dice_num])


try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a nummerical respnse, such as 15.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}")