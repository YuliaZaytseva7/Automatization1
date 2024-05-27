#В файле объявите переменную catalog Переменная хранит в себе список ([]).
#Наполните список пятью разными экземплярами класса Smartphone
#Напишите цикл, который печатает весь каталог (список) в формате 
#<марка> - <модель>. <номер телефона>

from smartphone import Smartphone

catalog =[]

phone1 = Smartphone("Apple", "iPhone12", "+79005004545")
phone2 = Smartphone("Xiaomi", "Redmi Note 3", "+79122345678")
phone3 = Smartphone("Samsung", "Galaxy X3", "+79563458787")
phone4 = Smartphone("Apple", "iPhone14", "+79003645353")
phone5 = Smartphone("Huawei", "P8 lite", "+79124546363")

catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(f"{phone.name}, {phone.type}, {phone.phone_number}")
    
