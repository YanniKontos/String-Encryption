import random
import string

from cryptography.fernet import Fernet

encryption_choice = input('would you like to choose your password? if no, it will be randomly generated [Y/N]')

if encryption_choice == 'Y':

    def inputted_password():
        pwd = input('enter your desired password')
        # created password

        encryption_key = Fernet.generate_key()
        # generated encryption key
        fernet = Fernet(encryption_key)
        # what's used to encrypt items

        encrypted_pwd = fernet.encrypt(pwd.encode())
        # inputted password now encrypted
        decrypted_pwd = fernet.decrypt(encrypted_pwd).decode()
        # inputted password now decrypted / normal input

        print('Your encrypted password is', encrypted_pwd)
        print('Your encryption key is:', encryption_key)

        option_two = input('would you like to decrypt your password? if yes, input your encryption key, if no, [N]')
        if option_two == "b'tYIuC3cvs4-BxBWsTihmIs70fOqJxqiMfSWdF7Vpi3Q='":
            print('your password is:', pwd)
        elif option_two == 'N':
            print('your password has not been decrypted')

    inputted_password()

elif encryption_choice == 'N':

    def create_password():
        alphabet = string.ascii_letters
        integers = string.digits
        symbols = '!@#$%^&*-_=+;:/'
        generator = alphabet + integers + symbols

        randomized_password = (random.choices(generator, k=12))
        password_string = ''.join(randomized_password)
        # generated password

        encryption_key = Fernet.generate_key()
        # generated encryption key
        fernet = Fernet(encryption_key)

        encrypted_password = fernet.encrypt(password_string.encode())
        # generated pwd now encrypted
        decrypted_password = fernet.decrypt(encrypted_password).decode()
        # generated password now decrypted

        print('Your generated password is:', password_string)
        print('Your password encrypted is:', encrypted_password)

    create_password()
