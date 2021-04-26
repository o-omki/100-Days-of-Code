import string

def encode_decode(command: str, text: str, shift: int):
    if command.lower().strip() == "encode":
        cipher_text = ""
        for letter in text:
            if letter not in alphabets:
                cipher_text += letter 
            else:  
                pos = alphabets.index(letter)
                new_pos = pos + shift
                if new_pos < 26:
                    cipher_text += alphabets[new_pos]
                else:
                    cipher_text += alphabets[new_pos - 26]
        print(f"The encoded text is {cipher_text}")

    elif command.lower().strip() == "decode":
        cipher_text = ""
        for letter in text:
            if letter not in alphabets:
                cipher_text += letter             

            else:
                pos = alphabets.index(letter)
                new_pos = pos - shift
                cipher_text += alphabets[new_pos]
        print(f"The decoded text is {cipher_text}")
    
    else:
        print("Incorrect input!")

alphabets = list(string.ascii_lowercase)
flag = 'y'
while flag.lower() == 'y':
    command = input("\nEnter 'encode' to encrypt the message; 'decode' to decrypt: \n")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift order: "))
    shift = shift % 26
    encode_decode(command, text, shift)
    flag = input("Do you want to retry (y/n)? ")


