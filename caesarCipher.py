import cipher
import inputValidation

def main():
    
    print("Caesar Cipher Encoder and Decoder!\nEncode or decode a message using Caeser cipher\n")

    # User selects mode (validated to only accept "encode" or "decode")
    mode = inputValidation.encodeDecodeValidation() 
    ciphertext_plaintext = "ciphertext" if mode == "decode" else "plaintext"

    message = inputValidation.messageValidation(ciphertext_plaintext) # User enters a message to encode/ decode (validated to ensure a message is entered)

    shift = inputValidation.shiftValidation() # User enters a shift (validated to only accept an integer between 1 - 25)

    cipher.caesarCipher(mode, message, shift) # caesarCipher function to encode/ decode message

if __name__ == "__main__":
    main()