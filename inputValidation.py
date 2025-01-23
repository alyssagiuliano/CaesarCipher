def encodeDecodeValidation():
    while True:
        encode_decode = input("Encode or decode: ").lower()
        if encode_decode == "encode" or encode_decode == "decode":
            return encode_decode
        else:
            print("Please enter either encode or decode")

def messageValidation(ciphertext_plaintext):
    while True:
        message = input(f"Enter your {ciphertext_plaintext} message: ")
        if len(message) != 0:
            return message
        else:
            print(f"Please enter your {ciphertext_plaintext} message")

def shiftValidation():
    while True:
        try:
            shift = int(input("Enter shift (integer between 1 - 25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter an integer between 1 - 25")
        except ValueError:
            print("Please enter an integer between 1 - 25")

            