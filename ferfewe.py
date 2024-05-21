# получить от пользователя оценку

rate = input("Оцените работу оператора от 1 до 5:")
rate_as_number = int(rate)


# проверить, что оцнека от 1 до 5
if (rate_as_number<1):
    rate_as_number=1

if (rate_as_number>5):
    rate_as_number=5

print (rate_as_number)
 
# в зависимости от оценки предложить дать обратную связь

feedback = " "

if rate == 1:
    feedback = input("Расскажите, что нам улучшить?")

print(feedback)