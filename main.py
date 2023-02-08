import random
import colorama

from colorama import Fore
colorama.init()

num1 = random.randint(2, 8)
num2 = random.randint(2, 8)
num3 = random.randint(2, 8)

print("|", num1 - 1, "|", num2 - 1, "|", num3 - 1, "|")
print("-------------", Fore.CYAN + "")
print("|", num1, "|", num2, "|", num3, "|" + colorama.Style.RESET_ALL)
print("-------------")
print("|", num1 + 1, "|", num2 + 1, "|", num3 + 1, "|")