import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_presence_photo_pets(my_pets):
   '''Поверяем, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''
   wait = WebDriverWait(pytest.driver, 10)
   element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistics = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
   # Вывели элементы в переменную - statistics

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
   # Сохранили элементы *.img в переменную - images

   number = statistics[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   # Из данных статистики вывели количество питомцев пользователя
   half = number // 2
   # и вывели половину питомцев от общего количества

   number_of_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_of_photos += 1
   # Вывели питомцев с фотографией

   assert number_of_photos >= half
   print(f'количество фото: {number_of_photos}')
   print(f'Половина фото из числа питомцев: {half}')
   # Вывели проверку того, что количество питомцев с фотографией больше/равно половине общего количества питомцев пользователя

# Для запуска теста через терминал используем:
# python -m pytest -v --driver Chrome --driver-path c:\chromedriver/chromedriver.exe tests/test_some_pets_have_photos.py