import pytest
import time
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_show_pet_friends():
   '''Проверка перехода на страницу пользователя'''
   # установка неявного ожидания
   #pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   time.sleep(5)

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   time.sleep(5)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   time.sleep(5)
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   # images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   # names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   # descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   #
   # for i in range(len(names)):
   #    assert images[i].get_attribute('src') != ''
   #    assert names[i].text != ''
   #    assert descriptions[i].text != ''
   #    assert ', ' in descriptions[i]
   #    parts = descriptions[i].text.split(", ")
   #    assert len(parts[0]) > 0
   #    assert len(parts[1]) > 0





# Для запуска теста через терминал используем команду:
# python -m pytest -v --driver Chrome --driver-path c:\chromedriver/chromedriver.exe tests/test_show_pet_friends.py