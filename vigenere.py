import sys
# Vigenere cipher

""" Table-based solver
def create_table(key):
    table = []
    for i in range(len(key)):
        table.append([])
        offset = LETTER_CODES[key[i]]
        for j in range(len(LETTERS)):
            table[i].append(LETTERS[(j+offset)%len(LETTERS)])
    return table

def solver_1(table,cipher):
    solved = ""
    for i in range(len(cipher)):
        solved += table[i%len(table)][LETTER_CODES[cipher[i]]]
    return(solved)
"""

def encode(text,key): # Encodes plaintext using a given key
    cipher = "" # The encoded plaintext
    for i in range(len(text)): # Iterate over the plaintext
        if(text[i] in LETTER_CODES_HIGH): # If the current character is uppercase
            cipher += LETTERS_HIGH[(LETTER_CODES_HIGH[text[i]]+(LETTER_CODES_HIGH[(key[i%len(key)]).upper()]))%len(LETTERS_HIGH)]
        elif(text[i] in LETTER_CODES_LOW): # If the current character is lowercase
            cipher += LETTERS_LOW[(LETTER_CODES_LOW[text[i]]+(LETTER_CODES_LOW[(key[i%len(key)]).lower()]))%len(LETTERS_LOW)]
        else: # The current character is not a letter
            cipher += text[i] # Don't convert non-letter characters    
    return cipher

def decode(cipher,key): # Decodes encoded text using a given key
    text = "" # The decoded cipher
    for i in range(len(cipher)): # Iterate over the plaintext
        if(cipher[i] in LETTER_CODES_HIGH): # If the current character is uppercase
            text += LETTERS_HIGH[(LETTER_CODES_HIGH[cipher[i]]-(LETTER_CODES_HIGH[(key[i%len(key)]).upper()]))%len(LETTERS_HIGH)]
        elif(cipher[i] in LETTER_CODES_LOW): # If the current character is lowercase
            text += LETTERS_LOW[(LETTER_CODES_LOW[cipher[i]]-(LETTER_CODES_LOW[(key[i%len(key)]).lower()]))%len(LETTERS_LOW)]
        else: # The current character is now a letter
            text += cipher[i] # Don't convert non-letter characters
    return text
        

# Uppercase letters
LETTERS_HIGH = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# Lowercase letters
LETTERS_LOW = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z']
LETTER_CODES_HIGH = {} # Stores numerical values of uppercase letters
LETTER_CODES_LOW = {} # Stores numerical values of lowercase letters

for i in range(len(LETTERS_HIGH)): # Builds lower- and uppercase dictionaries letter values.
    LETTER_CODES_HIGH[LETTERS_HIGH[i]] = i
    LETTER_CODES_LOW[LETTERS_LOW[i]] = i

task = sys.argv[1]
key = sys.argv[2]
#text = "MYMESSAGE"
#cipher = encoder(text,key)
if(task == "-e"):
    while(True):
        print(encode(input(),key))
elif(task == "-d"):
    while(True):
        print(decode(input(),key))
#print(cipher)
#print(decoder(cipher,key))
