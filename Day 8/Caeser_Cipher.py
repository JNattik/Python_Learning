alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

question = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
if question.lower() == "encode":
    message = input("Type your message: ")
    shift_n = input("Type the shift number: ")

    number_of_digits_message = len(message)

    while number_of_digits_message > 0:
        for x in message:
            letter = message[x]
            letter += shift_n
        
        


    result_question = input("Teype 'yes' if you want to go again. Otherwise type 'no'")
    if result_question == "yes":
        question2 = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    else:
        print("Congratulations, you are done!")

else:
    message = input("Type your message: ")
    shift_n = input("Type the shift number: ")