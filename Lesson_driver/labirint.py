from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Зайти на лабиринт ру
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.labirint.ru")

#найти книги по слову python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("python", Keys.RETURN)

#собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

#вывести в консоль инфо: название + автор + цена
for book in books:
    title = book.find_element(By.CSS_SELECTOR,".product-card__name").text
    author = book.find_element(By.CSS_SELECTOR,"div.product-card__author").text
    price = book.find_element(By.CSS_SELECTOR,"div.product-card__price-current").text
    print(author + "\t" + title + "\t" + price)






sleep(5)

