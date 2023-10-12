import caesarcipher
import vigenere
import XORcipher

def choose_cipher():
    while True:
        choice = input('''Choose the Encryption method you\'d like to explore:
        1. Ceasar Cipher
        2. Vigenère Cipher
        3. XOR Cipher
        
        ''')

        if choice in ('1','2','3'):
            return int(choice)
        print('\nPlease choose a valid item')

def replay():
    while True:
        re = input('Would you like to explore another form of encryption? (\'y\' or \'n\'): ')
        if re.startswith('y') or re.startswith('n'):
            return re.startswith('y')
        print('\nInvalid input')

def main():
    
    print('''Welcome to this Keith\'s Cryptography Castle! This app was made for 2 purposes:

        1. To teach Python code - The algorithms implemented in this program demonstrate numerous useful code techniques that can be used by teachers for demonstration or code analysis exercises
        2. To teach basic Encryption concepts and methods
    
    This app includes 3 encryption methods, each including a brief description and tutorial. The 3 methods are:
    
        1. Ceasar Cipher (The earliest and most basic form of encryption originating in ancient Rome)
        2. Vigenère Cipher (A more advanced form of polyalphabetic substitution cipher, originating in Italy in 1553)
        3. XOR Cipher (An additive cipher from the late 18th - early 19th century)''')
    
    while True:
    
        choice = choose_cipher()
    
        if choice == 1:
            ceasarcipher.main()
        if choice == 2:
            vigenere.main()
        if choice == 3:
            XORcipher.main3()
        
        repeat = replay_01()
    
        if not repeat:
            print('Bye then!')
            break

if '__name__' == __main__:
    main()
