import random
from typing import final

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "Y", "Z"]
symbol = ["@", "#", "$", "&", "*", "(", ")", "-", "_", "!"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = []
final_password = ""

print(
    '''  ____                                     _    ____                           _             
 |  _ \ __ _ ___ _____      _____  _ __ __| |  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| |  __/ | | |  __/ | | (_| | |_ (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                             '''
)

#User input the number
letter_choose = int(input("How many letter you want: "))
symbol_choose = int(input("How many symbol you want: "))
number_choose = int(input("How many number you want: "))

#logic to choose in the different list

for number in range(0, letter_choose):
    password += random.choice(letter)
for number in range(0, symbol_choose):
    password += random.choice(symbol)
for number in range(0, number_choose):
    password += random.choice(str(number))
for number in range(0,  len(password)):
    final_password += random.choice(password)

#print the final password
print(f"The new password is: {final_password}")


