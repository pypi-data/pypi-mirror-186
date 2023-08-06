"""
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by wual)
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
    
See proyect >> https://github.com/14wual/pycryptools
Follow me >> https://twitter.com/codewual
"""
# --------------------Extern Imports--------------------
import sys

# --------------------Intern Imports--------------------
from pycryptools.alberti import Alberti
from pycryptools.atbash import Atbash
from pycryptools.caesar import Caesar
from pycryptools.jefferson import Jefferson
from pycryptools.letter_number import LetterNumber
from pycryptools.morse import Morse
from pycryptools.polybios import Polybios
from pycryptools.scytale import Scytale
from pycryptools.vigenere import Vigenere

# --------------------APP--------------------
def Command():
    """Usage command --algorithm -mode message """
        
    algorithm = str(sys.argv[1])
    mode = str(sys.argv[2])
    message = str(sys.argv[3])
    
    avilable_algorithm = ["--atbash", "--scytale", "--polybios", "--caesar", "--alberti", "--jefferson", "--vigenere", "--morse", "--letter-to-number"]
    avilable_modes = ["-e","-d","-n"]
    
    print_modes = "Avilable Modes:\
            \n-e    [for encrypt]\
            \n-d    [for decrypt]\
            \n-n    [none mode]"
            
    print_algorithm = "Avilable Algorithm:\
            \n--atbash\
            \n--scytale\
            \n--polybios\
            \n--caesar\
            \n--alberti\
            \n--jefferson\
            \n--vigenere\
            \n--morse\
            \n--letter-to-number"
    
    if algorithm not in avilable_algorithm:
        
        print("[ERROR] | Choose a correct algorithm.")
        
        print(print_algorithm)
        
        return AssertionError, "Wrong algorithm"
    
    else: print(f"Algorithm: {algorithm}")
    
    if mode not in avilable_modes:
        
        print("[ERROR] | Choose a correct mode.")
        
        print(print_modes)

        return AssertionError, "Wrong mode"
    
    else: print(f"Mode: {mode}")
    
    print(f"Message: {message}")
    
    if mode == "-e":
        
        if algorithm == "--atbash":print("Encrypt: ", Atbash.encrypt(message))
        
        elif algorithm == "--scytale":
            key = input("Write your key: ")
            print(Scytale.encrypt(message, str(key)))
        
        elif algorithm == "--polybios":print("Encrypt: ", Polybios.encrypt(message))

        elif algorithm == "--caesar":
            key = input("Write your key: ")
            print(Caesar.encrypt(message, int(key)))
        
        elif algorithm == "--alberti":print("Encrypt: ", Alberti.encrypt(message))
        
        elif algorithm == "--jefferson":print("Encrypt: ", Jefferson.encrypt(message))
        
        elif algorithm == "--vigenere":
            key = iey = input("Write your key: ")
            print("Encrypt: ", Vigenere.encrypt(message, str(key)))
        
        elif algorithm == "--morse":print("Encrypt: ", Morse.encrypt(message))
        
        elif algorithm == "--letter-to-number":print("Encrypt: ", LetterNumber.encrypt(message))
        
    elif mode == "-d":
        
        if algorithm == "--atbash":print("Decrypt: ", Atbash.decrypt(message))
        
        elif algorithm == "--scytale":
            key = input("Write your key: ")
            print("Decrypt: ", Scytale.decrypt(message, str(key)))
        
        elif algorithm == "--polybios":print("Decrypt: ", Polybios.decrypt(message))
        
        elif algorithm == "--caesar":
            key = input("Write your key: ")
            print("Decrypt: ", Caesar.decrypt(message, int(key)))
        
        elif algorithm == "--alberti":print("Decrypt: ", Alberti.decrypt(message))
        
        elif algorithm == "--jefferson":print("Decrypt: ", Jefferson.decrypt(message))
        
        elif algorithm == "--vigenere":
            key = iey = input("Write your key: ")
            print("Decrypt: ", Vigenere.decrypt(message, str(key)))
        
        elif algorithm == "--morse":print("Decrypt: ", Morse.decrypt(message))
        
        elif algorithm == "--letter-to-number":print("Decrypt: ", LetterNumber.decrypt(message))
        
    elif mode == "-n":
        if algorithm in avilable_algorithm:print(algorithm.upper(), "Need a mode [-e/-d].")
        
    
if __name__ == '__main__':
    Command()