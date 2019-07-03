import math
from random import randint
upper = 1024
secret = randint(1 , upper)
print(secret)
limit = int(math.log(upper))
win = 0
for i in range(limit):
    guess = int (input("guess number PLZ:\n"))
    if guess <secret :
        print("yuor number less than pc numbers \n")
    elif guess > secret:
        print("your number greater than Pc number \n")
    else:
        win = 1
        break
if win == 1:
    print("Bingo")
else:
    print("Haaaa Haaaaa")