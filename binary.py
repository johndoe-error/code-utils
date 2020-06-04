def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

mode = ""
def setup():
    mode = input ("Выберите режим работы (зашифровать/расшифровать) и введите 1 или 2: ")
    if mode == "1" or mode == "2":
        if mode == "1":
            encode = input("Введите текст: ")
            print('Результат: ' + text_to_bits(encode))
        if mode == "2":
            decode = input("Введите двоичный код: ")
            print('Результат: ' + text_from_bits(decode))
    else:
        print("Неправильный режим выбран. Попробуйте еще раз!")

print('''   
██████╗░██╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗
██╔══██╗██║████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
██████╦╝██║██╔██╗██║███████║██████╔╝░╚████╔╝░
██╔══██╗██║██║╚████║██╔══██║██╔══██╗░░╚██╔╝░░
██████╦╝██║██║░╚███║██║░░██║██║░░██║░░░██║░░░
╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
         Telegram: @ENTER_ERROR          
            ''')

while mode != "1" or mode != "2":
    setup()

    
