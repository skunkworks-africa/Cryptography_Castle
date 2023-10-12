import string
from random import randint
import ast
import shlex

def convert_bin(text):
    # Save each character's binary as item in list
    split = [format(ord(l),'b') for l in text]
    
    # If any binary string has length of < 7, add 0's to start
    for ind,item in enumerate(split):
        if len(item) < 7:
            diff = 7-len(item)
            add = '0'*diff
            split[ind] = add+item            
            
    return " ".join(split)

def convert_ascii(binary):
    if ' ' in binary:
        return "".join(chr(int(b,2)) for b in binary.split())
    else:
        return chr(int(binary,2))

def key_gen():
    
    byte = ''
    
    for i in range(7):
        byte += str(randint(0,1))
        
    return byte

def input_key(text):
    while True:
        key = input('\nEnter your key (Leave blank if you wish to generate a random key): ')
        if '\\' in key:
            key = ast.literal_eval(shlex.quote(key))
        if len(key) == len(text) or not key:
            return key
        print('\nThe length of your key needs to match the length of your text')

def match(c1,c2):
    return c1 == c2

def xor_encrypt(text,key=''):
    
    bin_text = convert_bin(text)
    key = " ".join(key_gen() for x in text) if not key else key
    encrypted_bin = ''
    
    for i,c in enumerate(bin_text):
        
        if c == ' ':
            encrypted_bin += c
        else:
            encrypted_bin += '0' if match(bin_text[i],key[i]) else '1'
            
    print(f'\nBinary Representation of Text: {bin_text}')
    print(f'\nBinary Representation of Key:  {key}')
    print(f'\nXOR Encryption Binary Outcome: {encrypted_bin}')
    
    return convert_ascii(encrypted_bin), convert_ascii(key)

def replay():
    while True:
        re = input('Go again? (\'y\' or \'n\'): ')
        if re.startswith('y') or re.startswith('n'):
            return re.startswith('y')
        print('Invalid input')

def main_03():
    
    print('''Welcome to XORCrypt!
    
    This program is designed to teach encryption concepts as well as Python code.
    Here is a brief walkthrough of how XOR encryption works and how it is implemented in this code:
    
    1. The user must first input a text
    2. This program will convert the text into a 7-bit binary string
    3. This program generates a key of random 1's and 0's to match the length of the binary text.
    4. The encryptor will then iterate over the binary of the text and generated a 1 or 0 according to this table:

        Plaintext | Key | Ciphertext
            0     |  0  |     0
            1     |  1  |     0
            0     |  1  |     1
            1     |  0  |     1
            
    5. The resulting cipher binary is then converted to ascii
    6. This program returns the ciphertext and the randomly generated encryption key to the user for decryption purposes
    
    I hope this made sense. Enjoy!\n''')
    
    while True:
        
        text = input("Enter the text: ")
        if '\\' in text:
            text = ast.literal_eval(shlex.quote(text))
        
        key = input_key(text)
            
        cipher, key = xor_encrypt(text,convert_bin(key))
        
        
        print(f'\nEncrypted Text: {repr(cipher)}')
        print(f'ASCII Key: {repr(key)}')
              
        repeat = replay()
              
        if not repeat:
              break

if __name__ == "__main__":
    main()
