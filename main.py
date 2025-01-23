import cipher

def main():
    
    print("Caesar Cipher Encoder or Decoder!\nEncode or decode a message using Caeser cipher")

    encode_decode = input("Encode or decode: ").lower() # User selects encode or decode
    message = input("Enter message: ") # User enters a message to encode/ decode
    shift = int(input("Enter shift (between 1 - 25): ")) # User selects a shift

    cipher.caesarCipher(encode_decode, message, shift)

if __name__ == "__main__":
    main()