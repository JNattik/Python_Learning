import pandas

data = pandas.read_csv("./Day 26/nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

code_list = data["code"].to_list()
letter_list = data["letter"].to_list()

new_dict = {y.letter:y.code for (x,y) in data.iterrows()}

input_name = input("What is your name? ").upper()

new_list = [new_dict[x] for x in input_name]
print(new_list)

#for x in input_name:
    #print(new_dict[x])