#Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму, 
#которая будет на счету пользователя спустя Y лет.

def bank(x,y):
    account = x
    for i in range(y):
        account=account*1.1
    return account

print(bank(5000,2))