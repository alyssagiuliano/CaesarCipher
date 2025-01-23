def caesarCipher(encode_decode, message, shift):

    output = ""

    if encode_decode == "decode":
        # Makes shift a negative, hence shifts alphabet back and decodes (rather than encodes)
        shift = shift*-1 

    for char in message:
        # If character is uppercase, start is 65 (ASCII A), else its 97 (ASCII a)
        start = 65 if char.isupper() else 97

        if char.isalpha() == False:
            output += char 
        else:
            # ord(char): converts character into ASCII value
            # - start: maps value within a range of 0 - 25
            # + (encode)/ - (decode) shift: shifts the letter in the alphabet
            # %26: ensure results stay within bounds of alphabet (wraps if past z/Z)
            # + start: shifts value back to ASCII value
            # wrapped in chr(): to convert ASCII value back to a character
            # character then appended to output
            output += chr((ord(char) - start + shift) % 26 + start)
    print(output)