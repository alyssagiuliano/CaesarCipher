import cipher

def main():
    
    print("Caesar Cipher Encoder and Decoder!\nEncode or decode a message using Caeser cipher\n")

    encode_decode = input("Encode or decode: ").lower() # User selects encode or decode
    ciphertext_plaintext = "ciphertext" if encode_decode == "decode" else "plaintext"

    message = input(f"Enter your {ciphertext_plaintext} message: ") # User enters a message to encode/ decode
    shift = int(input("Enter shift (between 1 - 25): ")) # User enters a shift

    cipher.caesarCipher(encode_decode, message, shift) # caesarCipher function encodes/ decodes message

if __name__ == "__main__":
    main()