from pyfiglet import Figlet
import random
import vk_api
import time
import os
import sys
import shutil
import traceback

while True:
    os.system('clear') 
    f = Figlet(font='ascii___')

    def DrawText(text,center=True):
        if center:
            print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText(text).split("\n")],sep="\n")  
        else:
            print(f.renderText(text))
    DrawText('666',center=True)
    print("\033[35m{}\033[0m".format("\nДанный скрипт написал DARKNESSS666🦋."))
    print('''\n[1] Накрутка сообщениями.
[2] Накрутка стикерами.
[3] Помощь.''')
    choice = input("\nВведите нужную цифру: ")
    if choice == "1" or choice == "один" or choice == "Один":
        os.system('clear')
        tg = input("\033[33m{}\033[0m".format("Хочешь добавить автора скрипта в друзья в ВК? [y/n]"))
        if tg == "y" or tg == "Y":
            os.system("termux-open-url 'https://vk.com/i_am_sorry_but_my_life_is_shit'")
            print("\033[32m{}\033[0m".format("Правда, я лучший?<3"))
            TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
            user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
            posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
            msgs = input("\033[33m{}\033[0m".format("🔆Введи комментарий накрутки: "))
            print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + z + enter."))
            apivk = vk_api.VkApi(token=TOKEN).get_api()
        elif tg == "n" or tg == "N":
            print("\033[31m{}\033[0m".format("Ну не хочешь, как хочешь(("))
            TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
            user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
            posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
            msgs = input("\033[33m{}\033[0m".format("🔆Введи комментарий накрутки: "))
            print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + z + enter.")) 
            apivk = vk_api.VkApi(token=TOKEN).get_api()
        while True:
            try:
                apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999))
                print(time.strftime("\033[36m[%d.%m.%Y|%H:%M:%S]", time.localtime()), "1 комм был отправлен.")
            except vk_api.exceptions.VkApiError as e:
                if e.code == 5:
                    print("\033[31m{}\033[0m".format("Вы ввели неверный токен."))
                    break
            except:
                traceback.print_exc()
                break
            time.sleep(3)
    if choice == "2" or choice == "два" or choice == "Два":
        os.system('clear')
        tg = input("\033[33m{}\033[0m".format("Хочешь добавить автора скрипта в друзья в ВК? [y/n]"))
        if tg == "y" or tg == "Y":
            os.system("termux-open-url 'https://vk.com/i_am_sorry_but_my_life_is_shit'")
            print("\033[32m{}\033[0m".format("Правда, я лучший?<3"))
            TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
            user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
            posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
            msgs = input("\033[33m{}\033[0m".format("🔆Введи айди стикера для накрутки: "))
            print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + z + enter."))
            apivk = vk_api.VkApi(token=TOKEN).get_api()
        elif tg == "n" or tg == "N":
            print("\033[31m{}\033[0m".format("Ну не хочешь, как хочешь(("))
            TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
            user_id = input("\033[33m{}\033[0m".format("🔆Введи айди страницы: "))
            posts_id = input("\033[33m{}\033[0m".format("🔆Введи айди поста: "))
            stickers = input("\033[33m{}\033[0m".format("🔆Введи айди стикера для накрутки: "))
            print("\033[1;33m{}\033[0m".format("Чтобы остановить скрипт нажми ctrl + z + enter.")) 
            apivk = vk_api.VkApi(token=TOKEN).get_api()
        while True:
            try:
                apivk.wall.createComment(owner_id=user_id, post_id=posts_id, sticker_id=stickers, guid=random.randint(0, 9999999999))
                print(time.strftime("\033[36m[%d.%m.%Y|%H:%M:%S]", time.localtime()), "1 стикер был отправлен.")
            except vk_api.exceptions.VkApiError as e:
                if e.code == 5:
                    print("\033[31m{}\033[0m".format("Вы ввели неверный токен."))
                    break
            except:
                traceback.print_exc() 
            time.sleep(3)
    if choice == "3" or choice == "три" or choice == "Три":
        os.system('clear')
        print("\033[32m>\033[0mИтак, если ты хочешь накручивать свои комментарии своим же текстом, то на главной странице скрипта вводи: 1\nЕсли ты хочешь накручивать свои комментарии каким-либо стикером, то вбей: 2\n \n\033[32m>\033[0mГде взять токен?\nВот тут - https://vkhost.github.io/. Нам нужен токен kate mobile, его нужно обрезать перед тем, как ввести его в нужную строчку для токена, как же его обрезать? Покажу на примере:\nhttps://oauth.vk.com/blank.html#access_token=c8fec353807dsjsbxvhwkzbac7130b5a118ehbd280fbe3f6dca672jehe1102c53db9604e73hdhsb0c4f071c6c&expires_in=0&user_id=677429448.\nВот нам дан рандомный токен, нам нужна часть с \033[1maccess_token= \033[0mдо \033[1m&expires_in \033[0m, но не включая эти части, то есть в данном случае правильно обрезанный токен будет такой:\nc8fec353807dsjsbxvhwkzbac7130b5a118ehbd280fbe3f6dca672jehe1102c53db9604e73hdhsb0c4f071c6c.\n \n\033[32m>\033[0mКак узнать айди поста? Скопируйте ссылку на нужный пост, куда будут крутиться комментарии или стикеры и вам нужно ввести те цифры, которые будут после последнего нижнего подчеркивания, давайте также рассмотрим на примере:\nhttps://vk.com/wall6712776_103\nВот у нас есть ссылка на пост, нам в данном случае нужны цифры 103, их нам и нужно будет в дальнейшем ввести.\n \n\033[32m>\033[0mАйди вашей страницы вы можете узнать в интернете.\n \n\033[32m>\033[0mАйди стикера вы также можете узнать в интернете.\n \nДумаю, вопросов остаться больше не должно.")
    start = input('Введите слово "\033[32mначало\033[0m" без кавычек, чтобы включить скрипт заново или "\033[31mвыход\033[0m", чтобы выйти из скрипта: ')
    if start == "начало" or start == "Начало":
        False
    if start == "выход" or start == "Выход":
        os.system('clear')
        exit()
