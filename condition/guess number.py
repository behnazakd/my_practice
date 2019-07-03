from random import randint
upper = 1024
secret = randint(1 , upper)
print(secret)
while True:
    guess = int (input("guess number PLZ:\n"))
    if guess <secret :
        print("yuor number less than pc numbers \n")
    elif guess > secret:
        print("your number greater than Pc number \n")
    else:
        print("Bingo")
        break
