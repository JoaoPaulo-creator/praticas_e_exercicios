from selenium import webdriver
from selenium.webdriver.support.ui import Select  # a utilização deste método é viável para selecionar um determinado valor ou uma opção que fica dentro de um dropdown list
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')

# Digitando o endereço no campo "Digite um CEP ou um Endereço:"
logradouro = driver.find_element_by_id('endereco')
a = 'Nome da Rua'
time.sleep(0.8)
logradouro.clear()
logradouro.send_keys(a)

# As linhas abaixo servem para selecionar uma opção do campo "Esse CEP é de:"
time.sleep(1)
select = Select(driver.find_element_by_name('tipoCEP'))
select.select_by_index(0)
time.sleep(2)
select.select_by_visible_text('Localidade/Logradouro')

# Buscando o CEP digitado
time.sleep(1)
driver.find_element_by_id('btn_pesquisar').click()
time.sleep(1)


#Funções para validar se a consulta foi realizada conforme o esperado
def menorque2carac():
    try:
        mensagem = driver.find_element_by_class_name('msg')
        if mensagem.is_enabled() or mensagem.is_enabled():
            print('O logradouro informado possui menos de 2 caracteres')
    except NoSuchElementException:
        time.sleep(1)


def msg():
    try:
        message = driver.find_element_by_id('mensagem-resultado')
        if message.is_displayed() or message.is_enabled():
            print('O endereço foi consultado conforme o esperado')

    finally:
        pass


def msg_error():
    try:

        msg_erro = driver.find_element_by_id('')
        if msg_erro.is_displayed() or msg_erro.is_enabled():
            print('O endereço informado está incorreto')

    finally:
        pass


elemento = driver.find_element_by_id('mensagem-resultado')
#elemento_erro = driver.find_element_by_id('')

if elemento.is_displayed() or elemento.is_enabled():
    msg()

'''elif elemento_erro.is_enabled() or elemento_erro.is_displayed():
    msg_error()
'''
