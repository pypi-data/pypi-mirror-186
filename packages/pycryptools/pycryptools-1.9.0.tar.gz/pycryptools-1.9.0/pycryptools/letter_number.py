"""
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by wual)
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

Letter Number:
    Letter-to-number encryption consists of replacing each letter of the
    alphabet in a message with a specific number. It is a form of simple 
    substitution ignition in which a table of correspondence between letters
    and numbers is used to encrypt and decrypt the message.

See proyect >> https://github.com/14wual/pycryptools
Follow me >> https://twitter.com/codewual
"""

class LetterNumber:
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ"
    
    def encrypt_letter_to_number(plaintext):
        
        plaintext = plaintext.upper()
        
        ciphertext = []
        
        for letter in plaintext:
            
            if letter in LetterNumber.alphabet:ciphertext.append(str(LetterNumber.alphabet.index(letter)))
            
        return "-".join(ciphertext)

    def decrypt_letter_to_number(ciphertext):
        
        plaintext = ""
        
        for c in ciphertext.split("-"):
            
            if c.isnumeric():plaintext += LetterNumber.alphabet[int(c)]
            
        return plaintext
