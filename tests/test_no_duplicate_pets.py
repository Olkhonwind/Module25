import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(my_pets):
    '''Проверка отсутствия в списке пользователя повторяющихся питомцев'''

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # в переменную - pet_data cохранили элементы с данными о питомцах

    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)
    # Из полученных данных в pet_data оставили имя, возраст и породу, вместо не интересующих данных ставим пустую строку
    # и отделяем через пробел.

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '
    # Объединили полученные данные имени, возраста, породы.
    # Полученный результат добавили в строку с пробелом.

    list_line = line.split(' ')
    set_list_line = set(list_line)
    a = len(list_line)
    b = len(set_list_line)
    # из строки line вывели список, перевели его в множество и нашли количество элементов в списке и в множестве
    result = a - b
    assert result == 0
    # Нашли разницу в количестве элементов списка с количеством элементов множества
    # В случае, если разница между элементами равна 0, то повторяющиеся питомцы у пользователя отсутствуют

# Для запуска теста через терминал используем:
# python -m pytest -v --driver Chrome --driver-path c:\chromedriver/chromedriver.exe tests/test_no_duplicate_pets.py