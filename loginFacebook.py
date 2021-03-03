from selenium import webdriver
import time

driver = webdriver.Chrome('X:\caminho\do\chromedriver.exe')
driver.maximize_window()
url = 'https://www.facebook.com/'
driver.get(url)

usr = 'seu@email.com'
psw = 'suasenha'

email = driver.find_element_by_xpath('//*[@id="email"]')
senha = driver.find_element_by_xpath('//*[@id="pass"]')

try:
    #Se o elemento selecionado estiver habilitado ou visível, deverá ser possível digitar o email do usuário
    if email.is_displayed() or email.is_enabled():
        email.send_keys(usr)

finally:
    #Se o teste da condição acima for verdadeira, então deverá ser possível digitar a senha e realizar o login
    senha.send_keys(psw)
    time.sleep(2)
    driver.find_element_by_name('login').click()
