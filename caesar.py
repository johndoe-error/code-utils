blst = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
llst = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'] 

mode = ""
def setup():
    mode = input ("Выберите режим работы (зашифровать/расшифровать) и введите 1 или 2: ")
    if mode == "1" or mode == "2":
        frase = input("Введите фразу (без спец. символов): ")
        shift = int(input("Введите сдвиг: "))
        if mode == "1":
            print('Результат: ' + encryptCaesar(frase, shift))
        if mode == "2":
            print('Результат: ' + decryptCaesar(frase, shift))
    else:
        print("Неправильный режим выбран. Попробуйте еще раз!")

def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)%len(llst)
            ret += llst[(ind+shift)%len(llst)]
        elif x in blst:
            ind = blst.index(x)%len(llst)
            ret += blst[(ind+shift)%len(llst)]
        else:
            ret += x
    return ret
 
def decryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind-shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind-shift]
        else:
            ret += x
    return ret


print('''   
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
            Telegram: @ENTER_ERROR          
            ''')

        

while mode != "1" or mode != "2":
    setup()