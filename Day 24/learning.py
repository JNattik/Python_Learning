#Ad-ons to original Snake game from Day 21 were made
#with open("my_file.txt") as file:      #same as variable = open("") --> when done however, this method directly closes the file again
    #contents = file.read()
    #print(contents)

with open("my_file.txt", mode="a") as file:     #a = append, w = write
    file.write("New text.")