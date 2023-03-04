import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_present(my_pets):
   '''Проверка наличия всех питомцев на странице со списком питомцев пользователя'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   # Элементы карточек питомцев вывели в переменную - pets

   statistics = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
   # Вывели элементы в переменную - statistics

   number_of_pets = len(pets)
   # Вывели количество карточек питомцев пользователя

   number = statistics[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   # Из данных статистики вывели количество питомцев пользователя

   assert number == number_of_pets
   # Проверили совпадения количества питомцев из статистики с количеством карточек питомцев


# Для запуска теста через терминал используем:
# python -m pytest -v --driver Chrome --driver-path c:\chromedriver/chromedriver.exe tests/test_all_pets.py