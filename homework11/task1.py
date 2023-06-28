# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sleep(1)

try:
    # Переход в раздел Контакты
    driver.get('https://sbis.ru/')
    sleep(1)
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1 [href="/contacts"]')
    contacts.click()
    sleep(1)

    # Поиск баннера и клик по нему
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8')
    assert banner.is_displayed()
    banner.click()
    sleep(1)

    # Проверка отображения блока новости "Сила в людях"
    driver.switch_to.window(driver.window_handles[1])
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    assert news_block.is_displayed()
    name_block = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    news_name = name_block.text
    assert news_name == 'Сила в людях'
    assert name_block.is_displayed()

    # Переход по кнопке Подробнее
    more_button = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    scroll_to_element = more_button.location_once_scrolled_into_view
    sleep(1)
    more_button.click()
    sleep(1)

    # Проверка соответствия открытой ссылки
    link = 'https://tensor.ru/about'
    last_window = driver.current_url
    assert last_window == link, 'Вы перешли по неправильной ссылке'

finally:
    driver.quit()
