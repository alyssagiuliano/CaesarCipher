# Caesar Cipher Encoder and Decoder

This python program encodes or decodes user input using Caesar cipher.

## How to Run ##
Clone the [CaesarCipher repository](https://github.com/alyssagiuliano/CaesarCipher) from GitHub. Once cloned, naviagte inside the repository, and within your terminal run 

```bash
python caesarCipher.py
```

## Using the Program ##

Once the program is running, it will present the following message:

```python
"Caesar Cipher Encoder and Decoder!"
"Encode or decode a message using Caeser cipher"
```


It will then ask you for a series of inputs:
```python 
"Encode or decode:"
```

Your input should be either "Encode" or "Decode" (case not sensitive)
- Encode: Will ask for a plaintext message and encode it using Caesar cipher
- Decode: Will ask for a ciphertext message and will decode it using Caesar cipher

If you do not enter either "Encode" or "Decode", the program will prompt you to "Please enter either encode or decode" and try again.

```python 
"Enter your plaintext/ ciphertext message:"
```

Your input can be any message, with a combination of characters, numbers, spaces and/ or special characters

```python 
"Enter shift (integer between 1 - 25):"
```
The shift is the number of positions each letter in the plaintext is shifted along the alphabet to create the ciphertext. For example, if you shift is 3, the letter "a" is shifted to "d". Your input should be an integer between 1 and 25 (inclusive). 

If you do not enter an integer between 1 and 25 (inclusive), the program will prompt you to "Please enter an integer between 1 - 25" and will allow you to try again.

Once you have provided inputs for these questions, the program will either provide the encoded ciphertext of the plaintext message you entered, or the decoded plaintext of the ciphertext message you entered.



