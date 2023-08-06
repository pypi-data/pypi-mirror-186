"""
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by wual)
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

Vigenere:
    The Vigenère cipher is a polyalphabetic substitution encryption method that
    uses a key-based character substitution table. The table is built from a 
    character array, where each column represents a letter of the key and each row
    represents a letter of the alphabet.
    
See proyect >> https://github.com/14wual/pycryptools
Follow me >> https://twitter.com/codewual
"""

# --------------------Extern Imports--------------------
import itertools
import string

# --------------------APP--------------------
class Vigenere:
    
    def encrypt(message:str, key:str):
        
        assert isinstance(message, str), TypeError("The message argument must be a string.")
        
        key = itertools.cycle(key)
        
        ciphertext = ""
        
        for i, c in enumerate(message):
            
            shift = ord(next(key)) % ord('A')
            
            if c in string.ascii_uppercase:ciphertext += chr((ord(c) + shift - ord('A')) % 26 + ord('A'))
            elif c in string.ascii_lowercase:ciphertext += chr((ord(c) + shift - ord('a')) % 26 + ord('a'))
            else:ciphertext += c
            
        return ciphertext

    def decrypt(ciphertext:str, key:str):
        
        assert isinstance(message, str), TypeError("The message argument must be a string.")
        
        key = itertools.cycle(key)
        
        message = ""
        
        for i, c in enumerate(ciphertext):
            
            shift = ord(next(key)) % ord('A')
            
            if c in string.ascii_uppercase:message += chr((ord(c) - shift - ord('A')) % 26 + ord('A'))
            elif c in string.ascii_lowercase:message += chr((ord(c) - shift - ord('a')) % 26 + ord('a'))
            else:message += c
            
        return message
