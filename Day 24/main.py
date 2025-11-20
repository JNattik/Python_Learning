PLACEHOLDER = "[name]"

with open(file = "./Input/Names/names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents = file.read()
    for x in names:
        stripped_name = x.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)