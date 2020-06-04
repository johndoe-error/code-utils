# -*- coding: utf-8 -*-
import binascii

def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))

def hex2str(h):
    return binascii.unhexlify(h)

mode = ""
def setup():
    mode = input ("Выберите режим работы (зашифровать/расшифровать) и введите 1 или 2: ")
    if mode == "1" or mode == "2":
        if mode == "1":
            encode = input("Введите текст: ")
            print('Результат: ' + str2hex(encode).decode('utf-8'))
        if mode == "2":
            decode = input("Введите HEX-код: ")
            print('Результат: ' + hex2str(decode).decode('utf-8'))
    else:
        print("Неправильный режим выбран. Попробуйте еще раз!")

print('''   

░██████╗████████╗██████╗░██████╗░██╗░░██╗███████╗██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗╚════██╗██║░░██║██╔════╝╚██╗██╔╝
╚█████╗░░░░██║░░░██████╔╝░░███╔═╝███████║█████╗░░░╚███╔╝░
░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░██╔══██║██╔══╝░░░██╔██╗░
██████╔╝░░░██║░░░██║░░██║███████╗██║░░██║███████╗██╔╝╚██╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
         Telegram: @ENTER_ERROR          
            ''')

while mode != "1" or mode != "2":
    setup()