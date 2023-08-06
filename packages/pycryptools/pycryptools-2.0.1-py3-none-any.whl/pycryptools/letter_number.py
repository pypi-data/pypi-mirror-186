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
    
    def encrypt(message:str):
        
        assert isinstance(message, str), TypeError("The message argument must be a string.")
        
        message = message.upper()
        
        message = []
        
        for letter in message:
            
            if letter in LetterNumber.alphabet:message.append(str(LetterNumber.alphabet.index(letter)))
            
        return "-".join(message)

    def decrypt(message:str):
        
        assert isinstance(message, str), TypeError("The message argument must be a string.")
        
        message = ""
        
        for c in message.split("-"):
            
            if c.isnumeric():message += LetterNumber.alphabet[int(c)]
            
        return message
