import sys
print ("Hello and welcome to Pokegotchi. こんにちは、Pokegotchiへようこそ。")
name= input ("What would you like to call your Pokegotchi? あなたはあなたのポケッと呼びたいと思いますか？")
print ("Hello " + name)
print ("こんにちは " + name)

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
if feed== "Y":
    print ("Feeding is in Progress")
import time
print ("Feeding your Pokegotchi!  あなたのPokegotchiを与える！")
boom=20
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
    
happiness = 100
hunger = 100
thirst = 100
health = 100

while happiness >0:
 happiness -=1
 print (happiness)

while hunger >0:
 hunger -=1
 print (hunger)

while thirst >0:
 thirst -=1
 print (thirst)

while health >0:
 health -=1
 print (health)

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

sleep = input ("Would you like to make your Pokegotchi sleep? Pokegotchiを眠らせたいですか？")

if sleep== "Y":
    print ("Sleeping is in Progress! Do not Disturb!")
    import time
print ("Your Pokegotchi is Sleeping! あなたのPokegotchiは眠っている！")
boom=40
while boom >0:
    time.sleep(1)
    print(boom)
    boom -=1
