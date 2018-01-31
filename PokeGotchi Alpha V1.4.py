import webbrowser

ie = webbrowser.get(webbrowser.iexplore)
ie.open('https://github.com/GalaxyTheoryz/pokegotchi')




print ("POKEGOTCHI V1.4")
print ("********************************************************************************")

import sys
print ("Welcome to PokeGotchi! / (C) Patrick 2018 / You may find source code for this on https://github.com/GalaxyTheoryz/pokegotchi.")
print ("This edition comes with two languages, English and Japanese.")
print ("ENJOY!")
print ("PokeGotchiへようこそ！ /（C）Patrick 2018 /これのソースコードはhttps://github.com/GalaxyTheoryz/pokegotchiにあります。")
print ("このエディションには、英語と日本語の2つの言語があります。")
print ("楽しい！")
print ("********************************************************************************")
print ("********************************************************************************")
lic= input ("BY USING THIS PROGRAM, YOU ACCEPT THE LICENSE INCLUDED WITH THIS PROGRAM. A COPY CAN BE FOUND HERE: https://github.com/GalaxyTheoryz/pokegotchi/blob/master/LICENSE Y/N")
if lic=="N":
    print ("You Declined the License Agreement. Terminating Program..")
    sys.exit()
print ("********************************************************************************")
print ("********************************************************************************")



print ("Hello and welcome to Pokegotchi. こんにちは、Pokegotchiへようこそ。")
name= input ("What would you like to call your Pokegotchi? あなたはあなたのポケッと呼びたいと思いますか？")
gender= input ("What Gender is your Pokegotchi? Male / Female / Other? あなたのポケッとは何ですか？男性/女性/その他？")
print ("Hello User, I like your name, which is " + name)
print ("こんにちは " + name)
print ("Great Choice on your Gender, which is " + gender)

start= input ("Would you like to begin game Y/N? あなたはゲームを始めたいですか Y / N？")
if start== "N":
    print ("Bye Bye! バイバイ！")
    sys.exit()
if start == "Y":
   print ("────────▄███████████▄────────")
   print ("─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────")
   print ("────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────")
   print ("───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───")
   print ("──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──")
   print ("─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─")
   print ("██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██")
   print ("██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██")
   print ("██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██")
   print ("███████████░░███░░███████████")
   print ("██░░░░░░░██░░███░░██░░░░░░░██")
   print ("██░░░░░░░░██░░░░░██░░░░░░░░██")
   print ("██░░░░░░░░░███████░░░░░░░░░██")
   print ("─██░░░░░░░░░░░░░░░░░░░░░░░██─")
   print ("──██░░░░░░░░░░░░░░░░░░░░░██──")
   print ("───██░░░░░░░░░░░░░░░░░░░██───")
   print ("────███░░░░░░░░░░░░░░░███────")
   print ("─────▀███░░░░░░░░░░░███▀─────")
   print ("────────▀███████████▀────────")

   print ("That is your egg, take good care of it! それはあなたの卵です、それを世話してください！")

import time
print ("Time until egg hatch 孵化までの時間")
boom=60
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
    print ("Your egg is hatching... あなたの卵は孵化しています...")

print ("HATCH HATCH HATCH!! ハッチハッチハッチ!!")

print ("\:.             .:/")
print ("        \``._________.''/ ")
print ("         \             / ")
print (" .--.--, / ..:.   ..:. \\")
print ("/__:  /  | '::' . '::' |")
print ("   / /   |`.   ._.   .'|")
print ("  / /    |.'         '.|")
print (" /___-_-,|.\  \   /  /.|")
print ("      // |''\.;   ;,/ '|")
print ("      `==|:=         =:|")
print ("         `.          .'")
print ("           :-._____.-:")
print ("          `''       `''")

feed = input ("Would you like to feed your Pokegotchi? Y/N  あなたはPokegotchiを食べたいですか？ Y / N")
if feed=="N":
    sleep = input ("Would you like to make your Pokegotchi sleep? Pokegotchiを眠らせたいですか？")
if feed== "Y":
    print ("Feeding is in Progress")
    


print ("        \``._________.''/ ")
print ("         \             / ")
print (" .--.--, / ..:.   ..:. \\")
print ("/__:  /  | '::' . '::' |")
print ("   / /   |`.   ._.   .'|")
print ("  / /    |.'         '.|")
print (" /___-_-,|.\  \   /  /.|")
print ("      // |''\.;   ;,/ '|")
print ("      `==|:=         =:|")
print ("         `.          .'")
print ("           :-._____.-:")
print ("          `''       `''")

sleep = input ("Would you like to make your Pokegotchi sleep? Pokegotchiを眠らせたいですか？")

if sleep=="N":
    drink= input ("Your Pokegotchi requires a drink! Y/N? あなたのPokegotchiは飲み物が必要です！ Y / N？")
    
if sleep== "Y":
    print ("Sleeping in Progress.")
    print ("Your Pokegotchi has slept well. あなたのPokegotchiはよく眠っています。")

if sleep=="N":
    print ("Your PokeGotchi does require to sleep, if not they may die!")

    print ("HAPPINESS = 90, SLEEP = 20, THIRST = 50, HUNGER = 100")
    # Note to self: Put in variable at future stage.

drink= input ("Your Pokegotchi requires a drink! Y/N? あなたのPokegotchiは飲み物が必要です！ Y / N？")
if drink=="N":
    menu= input ("Welcome to your Main Menu, please select an option. 1 - Re-cycle through all options. 2 - Play. 3 - Exit. Please select a number. 4 - Health Status")
    
if drink=="Y":
    boom=10
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
    print ("Your PokeGotchi drank well! あなたのPokeGotchiはうまく飲んだ！")

menu= input ("Welcome to your Main Menu, please select an option. 1 - Re-cycle through all options. 2 - Play. 3 - Exit. Please select a number.")

if menu=="2":
    print ("Your PokeGotchi slept well! あなたのPokeGotchiはよく眠った！")

if menu=="5":
    specificfood= input ("What would you like your PokeGotchi to eat?")
    if specificfood=="Magnet":
        print ("Oh no! You killed your PokeGotchi!")
        sys.exit()
    print ("Yum!")
 

if menu=="3":
    sys.exit()
    
    
if menu=="4":
    print ("Getting your PokeGotchi's Health Status. Please Wait a while... あなたのPokeGotchiの健康状態を取得する。しばらくお待ちください...")
    print ("Your Health is currently 78")

menu= input ("Welcome to your Main Menu, please select an option. 1 - Re-cycle through all options. 2 - Play. 3 - Exit 4 - Health Status. Please select a number.")    

if menu=="4":
    print ("Getting your PokeGotchi's Health Status. Please Wait a while... あなたのPokeGotchiの健康状態を取得する。しばらくお待ちください...")
    print ("Your Health is currently 78")


if menu=="2":
    print ("Your PokeGotchi has Evolved! あなたのPokeGotchiは進化しました！")
    print ("░█▀▀▄░░░░░░░░░░░▄▀▀█")
    print ("░█░░░▀▄░▄▄▄▄▄░▄▀░░░█")
    print ("░░▀▄░░░▀░░░░░▀░░░▄▀")
    print ("░░░░▌░▄▄░░░▄▄░▐▀▀")
    print ("░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█")
    print ("░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█")
    print ("▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█")
    print ("█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀")
    print ("░▀▄░░▀░░▀▀▀░░▀░░░▄█▀")
    print ("░░░█░░░░░░░░░░░▄▀▄░▀▄")
    print ("░░░█░░░░░░░░░▄▀█░░█░░█")
    print ("░░░█░░░░░░░░░░░█▄█░░▄▀")
    print ("░░░█░░░░░░░░░░░████▀")
    print ("░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀ ")
    print ("Your PokeGotchi has evolved to Level CHILD! あなたのPokeGotchiはレベルチャイルドに進化しました！")

if menu=="1":
    feed = input ("Would you like to feed your Pokegotchi? Y/N  あなたはPokegotchiを食べたいですか？ Y / N")
if feed== "Y":
    print ("Feeding is in Progress")
import time
print ("Feeding your Pokegotchi!  あなたのPokegotchiを与える！")


print ("\:.             .:/")
print ("        \``._________.''/ ")
print ("         \             / ")
print (" .--.--, / ..:.   ..:. \\")
print ("/__:  /  | '::' . '::' |")
print ("   / /   |`.   ._.   .'|")
print ("  / /    |.'         '.|")
print (" /___-_-,|.\  \   /  /.|")
print ("      // |''\.;   ;,/ '|")
print ("      `==|:=         =:|")
print ("         `.          .'")
print ("           :-._____.-:")
print ("          `''       `''")



if sleep== "Y":
    print ("Sleeping is in Progress! Do not Disturb!")
    import time
print ("Your Pokegotchi is Sleeping! あなたのPokegotchiは眠っている！")
boom=40
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
print ("Your Pokegotchi has slept well. あなたのPokegotchiはよく眠っています。")

if sleep=="N":
    print ("Your PokeGotchi does require to sleep, if not they may die!")

    print ("HAPPINESS = 90, SLEEP = 20, THIRST = 50, HUNGER = 100")
    # Note to self: Put in variable at future stage.

drink= input ("Your Pokegotchi requires a drink! Y/N? あなたのPokegotchiは飲み物が必要です！ Y / N？")
if drink=="Y":
    boom=10
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
    print ("Your PokeGotchi drank well! あなたのPokeGotchiはうまく飲んだ！")


 

if menu=="3":
    sys.exit()
    
    
if menu=="4":
    print ("Getting your PokeGotchi's Health Status. Please Wait a while... あなたのPokeGotchiの健康状態を取得する。しばらくお待ちください...")
    print ("Your Health is currently 78")

menu= input ("Welcome to your Main Menu, please select an option. 1 - Re-cycle through all options. 2 - Play. 3 - Exit 4 - Health Status. Please select a number.")    

if menu=="4":
    print ("Getting your PokeGotchi's Health Status. Please Wait a while... あなたのPokeGotchiの健康状態を取得する。しばらくお待ちください...")
    print ("Your Health is currently 78")



menu= input ("Welcome to your Main Menu, please select an option. 1 - Re-cycle through all options. 2 - Play. 3 - Exit 4 - Health Status. Please select a number.")

    
if menu=="5":
    specificfood= input ("What would you like your PokeGotchi to eat?")
    if specificfood=="Magnet":
        print ("Oh no! You killed your PokeGotchi!")
        sys.exit()
    print ("Yum!")

