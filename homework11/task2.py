# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

driver = webdriver.Chrome()
sleep(1)

driver.get('https://fix-online.sbis.ru/')
sleep(1)

# Авторизация на сайте

login_field = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
login_field.send_keys('kuda', Keys.ENTER)
login_field = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
login_field.send_keys('a1s1d1f1g1', Keys.ENTER)
sleep(5)

# Переход в реестр "Контакты"

contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
assert contacts.is_displayed()
contacts.click()
sleep(2)

second_contacts = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"] .NavigationPanels-SubMenu__headTitle')
assert second_contacts.is_displayed()
second_contacts.click()
sleep(2)

# Отправка сообщения

add_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"] .controls-BaseButton__wrapper')
assert add_button.is_displayed()
add_button.click()
sleep(2)

search_field = driver.find_element(By.CSS_SELECTOR, '.addressee-Dialog-Stack .controls-Field.js-controls-Field')
assert search_field.is_displayed()

search_field.send_keys('Кудашов Алексей')
sleep(1)

choose_me = driver.find_element(By.CSS_SELECTOR, '.ws-flexbox.ws-flex-column.ws-flex-grow-1.person-BaseInfo__content')
name = driver.find_element(By.CSS_SELECTOR, '.controls-fontsize-l.ws-ellipsis')
assert name.get_attribute('title') == 'Кудашов Алексей'
sleep(1)
choose_me.click()
sleep(1)


message_field = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
sleep(1)
message_field.click()
sms = 'Сообщение самому себе'
message_field.send_keys(sms)
send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
sleep(1)
send_message.click()
sleep(1)

# Проверка наличия сообщения в реестре

messages = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
sleep(1)
my_message = messages[0]
my_message_text = messages[0].text
assert my_message_text == sms

# Удаление сообщения

action_chains = ActionChains(driver)
action_chains.move_to_element(my_message)
action_chains.context_click(my_message)
action_chains.perform()

delete_button = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
sleep(1)
delete_button.click()
sleep(1)

# Проверка отсутствия удаленного сообщения

other_messages = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
not_my_message = other_messages[0]
not_my_text = not_my_message.text
assert not_my_text != sms
