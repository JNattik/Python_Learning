alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#def encrypt(text, shift):
    #cipher_text = ""
    #for x in text:
        #position = alphabet.index(x)
        #new_position = position + shift
        #new_letter = alphabet[new_position]
        #cipher_text += new_letter
    #print(f"The encoded text is '{cipher_text}'")

#def decrypt(cipher_text, shift):
    #text2 = ""
    #for y in cipher_text:
       #position = alphabet.index(y)
        #new_position = position - shift
        #new_letter = alphabet[new_position]
        #text2 += new_letter
    #print(f"The original text is '{text2}'.")

#if direction == "encode":
    #encrypt(text = text, shift = shift)
#elif direction == "decode":
    #decrypt(cipher_text = text, shift = shift)

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for n in start_text:
        if n in alphabet:
            position = alphabet.index(n)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += n
    print(f"The {cipher_direction}d text is '{end_text}'.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 26
    caeser(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    result = input("Do you want to go again? Type 'yes' to continue, 'no' to stop: ")
    if result == "no":
        should_continue = False