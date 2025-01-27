
from art import *  # From art.py import everything to the main.py
import time        # To use time module firstly we should import it

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

is_program_on=True  # To create an infinitive loop


while is_program_on:   # While True/False
    print("\n"*50)     # To create a fresh screen
    print(caesar_cipher_program_logo)
    time.sleep(3)      # To wait 3 seconds before make other operation
    print("\n"*50)


    print(encrypt_or_decrypt_logo)
    operation=input("To encrypt write: encrypt , To decrypt write: decrypt : ")
    print("\n"*50)
    
    print(shift_amount_logo)
    # %len(alphabet) a perfect trick I explained it in the readme 
    shift_amount=int(input("How much do you want to shift? : "))%len(alphabet)   # Input's default data type is str but I need int data type because of that I added int before input
    print("\n"*50)

    print(text_logo)
    text=input("What is your text? : ")  
    print("\n"*50)     
            


    def encrypt():
        new_text=""   # to store letters
        for letter in text:
            new_index=alphabet.index(letter)+shift_amount
            new_letter=alphabet[new_index]
            new_text+=new_letter
        print(result)
        print(f"New text is: {new_text}")
        input("\nPress enter to continue...")


    def decrypt():
        new_text=""  # To store letters
        for letter in text:
            new_index=alphabet.index(letter)-shift_amount    # The only difference between encrypt and decrypt
            new_letter=alphabet[new_index]
            new_text+=new_letter
        print(result)
        print(f"New text is: {new_text}")
        input("\nPress enter to continue...")


    if operation=="encrypt":
        encrypt()
    else:
        decrypt()
    
    print("\n"*50)
    print(want_to_restart_logo)
    restart_program=input("Do you wanna restart program? (y/n) : ").lower()   # Whatever you write is going to be lowercase
    if restart_program=="n":
        print("\n"*50)
        print(bye_bye_logo)
        is_program_on=False   # To stop loop
    else:
        print("\n"*50)  # To create a fresh screen










