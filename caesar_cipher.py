'''
Below is a simple formulation of the popular Caesar's Cipher in python
under the direction of Al Sweigart. Kudos and creit to him and his team for
this.
'''

#Let's determine which symbols we would like to decipher
from cmath import e
from symtable import Symbol


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
print("The Caesar cipher encrypts letters by shifting them over by a")
print("key number. As an example, a key of two (2) means the letter A")
print("will be encrypted into c, the letter B into D")
print()

# Let the user enter if they are encrypting or decrypting. Keep asking until they've entered e or d
while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Please enter the letter e or d.")


# Let the user enter what key they'd like to use as a numeric value
while True:
    max_key = len(SYMBOLS) -1
    print("Please enter the key (1 to {}) to use.".format(max_key))
    response = input('> ').lower()
    if int(response) == 0:
        print("A key of zero will result in non-encryption.")
        print("Please enter a value greater than zero")
        response = int(input('> '))
        continue
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
    
# Enter the message to be encrypted/decrypted
print("Enter the message to {}.".format(mode))
message = input('> ').lower()

# Store the final en/decryption in a variable 
translated = ''

# Ecryption logic
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol) # get the key for the encryption
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if number is larger than the length of SYMBOLS
        # or less than zero:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        # add encrypted/decrypted number's symbol to translated variable
        translated = translated + SYMBOLS[num]
    else:
        # add the symbol without encryption/decryption:
        translated = translated + symbol

# print the translated message
print("I've translated the message:")
print(translated)
