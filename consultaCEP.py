from selenium import webdriver
from selenium.webdriver.support.ui import Select #a utilização deste método é viável para selecionar um determinado valor ou uma opção que fica dentro de um dropdown list
import time


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')


#Digitando o endereço no campo "Digite um CEP ou um Endereço:"
lograouro = driver.find_element_by_id('endereco')
lograouro.send_keys('Rua Antonio Rogerio da Silva Rosa')
#lograouro.send_keys('a')


# As linhas abaixo servem para selecionar uma opção do campo "Esse CEP é de:"
time.sleep(1)
select = Select(driver.find_element_by_name('tipoCEP'))
select.select_by_index(0)
time.sleep(2)
select.select_by_visible_text('Localidade/Logradouro')


#Buscando o CEP digitado
time.sleep(1)
driver.find_element_by_id('btn_pesquisar').click()


#Se o endereço digitado possuir menos que 2 caracteres, o script deve instruir um refresh na tela, caso o código dentro do bloco try for inválido, \n
# deverá ser retornado ao tester uma mensagem e o navegador será fechado

try:
    time.sleep(1)
    msg_alerta = driver.find_element_by_class_name('msg')
    if msg_alerta.is_enabled() or msg_alerta.is_displayed():
        driver.refresh()
except:
    print('Não funcionou')
    time.sleep(5)
    driver.quit()
