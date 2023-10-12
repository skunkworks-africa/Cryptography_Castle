import string

ALPHABET = string.ascii_lowercase

def build_key(text, key):
    new_key = ''
    key_index = 0

    for char in text:
        if char.isalpha():
            new_key += key[key_index].lower()
            key_index = (key_index + 1) % len(key)
        else:
            new_key += char

    return new_key

def vigenere_cipher(text, key, decrypt=False):
    result = []
    key = build_key(text, key)
    alphabet_len = len(ALPHABET)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ALPHABET.index(key[i]) if not decrypt else -ALPHABET.index(key[i])
            new_char = ALPHABET[(ALPHABET.index(char.lower()) + shift) % alphabet_len]

            if char.isupper():
                new_char = new_char.upper()

            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def replay():
    while True:
        re = input('Go again? (\'y\' or \'n\'): ')
        if re.startswith('y') or re.startswith('n'):
            return re.startswith('y')
        print('Invalid input')

def main():

    print('''Welcome to Vigenère Vault!
    
    This program is designed to teach encryption concepts as well as Python code.
    Here is a brief walkthrough of how Vigenère encryption works and how it is implemented in this code:
    
    1. The user must first input a text string
    2. The user must then input a text key
    3. This program will then compress or extend the key using replication until it matches the length of the text.
    4. The user will specify whether to use the encryption or decryption algorithm
    5. The program will then apply a shift to each letter of the text according to the corresponding letter of the key and the user's choice of encryption or decryption
    6. This program returns the ciphertext or plain text to the user
    
    I hope this made sense. Enjoy!\n''')

    while True:
        operation = input("Hello, user. Will you be encrypting or decrypting a message? (enter 'e' or 'd'): ").lower()

        if operation.startswith('e'):
            decrypt = False
        elif operation.startswith('d'):
            decrypt = True
        else:
            print("\nPlease enter 'e' for encryption or 'd' for decryption.\n")
            continue

        # Step 5: Input Text
        while True:
            text = input("Enter the text: ")
            if not text:
                print('Enter a text of at least 1 alphanumeric character.\n')
            else:
                break

        # Step 6: Input Encryption Key
        while True:
            key = input("\nEnter an encryption key: ")
            if not key:
                print("\nPlease enter a key of at least 1 character (longer key recommended).\n")
            elif not key.isalpha():
                print("\nYour key cannot contain numbers or special characters.\n")
            else:
                break

        # Step 7: Execute the Chosen Operation
        result = vigenere_cipher(text, key, decrypt)
        print('\nResult:', result, '\n')

        repeat = replay()
              
        if not repeat:
              break

if __name__ == "__main__":
    main()
