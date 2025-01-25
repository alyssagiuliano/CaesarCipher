def encodeDecodeValidation():
    while True:
        mode = input("Encode or decode: ").lower() # Gets user input, asking "Encode or decode:"
        if mode == "encode" or mode == "decode": # If input is "encode" or "decode"
            return mode # Return the mode that was input  
        else: # If input is not "encode" or "decode"
            print("Please enter either encode or decode") # Ask the user to input either "encode" or "decode" - loops back to input 

def messageValidation(ciphertext_plaintext):
    while True:
        message = input(f"Enter your {ciphertext_plaintext} message: ") # Gets user input, asking "Enter your plaintext/ ciphertext message"
        if len(message) > 0: # If user input message length is bigger than 0
            return message # Return the message that was input  
        else: # If input length is not greater than 0 
            print(f"Please enter your {ciphertext_plaintext} message") # Ask the user to input a message - loops back to input 

def shiftValidation():
    while True:
        try:
            shift = int(input("Enter shift (integer between 1 - 25): ")) # Gets user input, asking "Enter shift (integer between 1 - 25):"
            if 1 <= shift <= 25: # If input value is greater than or equal to 1, and less than or rqal to 25
                return shift # Return the shift value that was input  
            else: # If input value is less than 1, or greater than 25
                print("Please enter an integer between 1 - 25") # Ask the user to input an integer between 1 - 25 - loops back to input 
        except ValueError: # If inout value is not an integer
            print("Please enter an integer between 1 - 25") # Ask the user to input an integer between 1 - 25 - loops back to input 

            