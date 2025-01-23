import cipher
import inputValidation

def main():
    
    print("Caesar Cipher Encoder and Decoder!\nEncode or decode a message using Caeser cipher\n")

    # User selects encode or decode (validated to only accept "encode" or "decode")
    encode_decode = inputValidation.encodeDecodeValidation() 
    ciphertext_plaintext = "ciphertext" if encode_decode == "decode" else "plaintext"

    message = input(f"Enter your {ciphertext_plaintext} message: ") # User enters a message to encode/ decode

    shift = inputValidation.shiftValidation() # User enters a shift (validated to only accept an integer between 1 - 25)

    cipher.caesarCipher(encode_decode, message, shift) # caesarCipher function encodes/ decodes message

if __name__ == "__main__":
    main()