import base64

print('''   
██████╗░░█████╗░░██████╗███████╗░█████╗░░░██╗██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══╝░░██╔╝██║
██████╦╝███████║╚█████╗░█████╗░░██████╗░██╔╝░██║
██╔══██╗██╔══██║░╚═══██╗██╔══╝░░██╔══██╗███████║
██████╦╝██║░░██║██████╔╝███████╗╚█████╔╝╚════██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝░╚════╝░░░░░░╚═╝
           Telegram: @ENTER_ERROR          
            ''')

mode = ""
while mode != "1" or mode != "2":
    mode = input ("Выберите режим работы (зашифровать/расшифровать) и введите 1 или 2: ")
    if mode == "1" or mode == "2":
        if mode == "1":
            message = input("Введите ваше сообщение: ")
            message_bytes = message.encode('UTF-8')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('UTF-8')
            # encode, decode, вообще бойкот...
            print(base64_message)
            
        if mode == "2":
            base64_message = input("Введите BASE64: ")
            base64_bytes = base64_message.encode('UTF-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('UTF-8')
           # encode, decode, вообще бойкот...
            print(message)           
    else:
        print("Неправильный режим выбран. Попробуйте еще раз!")
# Бвъуцдгдуеп, батцхъдцэн! Юашцйн яъицфа яц бъгсдн @Mieri_1, ида-да увахц "Р батцхъэ!" Ь гашсэцяъп, дцтр атюсяеэъ... Уцхн ода багэцхярр, с щясиъд, гсюср гэашяср бсгжсэьс :) Яе ъэъ р дсьаы фсх, жцж :)
