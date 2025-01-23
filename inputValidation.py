def encodeDecodeValidation():
    while True:
        encode_decode = input("Encode or decode: ").lower()
        if encode_decode == "encode" or encode_decode == "decode":
            return encode_decode
        else:
            print("Please enter encode or decode")

def shiftValidation():
    while True:
        try:
            shift = int(input("Enter shift (between 1 - 25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter an integer between 1 - 25")
        except ValueError:
            print("Please enter an integer between 1 - 25")

            