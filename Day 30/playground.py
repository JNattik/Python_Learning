#File not Found error
# with open("file.txt") as file:
#    file.read()

#Key Error
# dictionary = {"key": "value"}
# value = dictionary["non_existing_key"]

#Index Error
# fruits = ["apple", "banana", "pineapple"]
# fruit = fruits[3]

#TypeError
# text = "abc"
# print(text + 5)

#Type Error
try:
     file = open("a_file.txt")
     a_dictionary = {"key": "value"}
     print(a_dictionary["key"])
except FileNotFoundError:
     file = open("a_file.txt", "w")
     file.write("Something")
except KeyError:
     print("That key does not exist.")
else:
     content = file.read()
     print(content)
finally:
     raise KeyError
     #file.close()
     #print("File was closed.")