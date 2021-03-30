from selenium import webdriver
from selenium.webdriver.support.ui import Select  # a utilização deste método é viável para selecionar um determinado valor ou uma opção que fica dentro de um dropdown list
import time
from selenium.common.exceptions import NoSuchElementException
'======================================================================================================================'
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
'======================================================================================================================'
# Digitando o endereço no campo "Digite um CEP ou um Endereço:"
logradouro = driver.find_element_by_id('endereco')
a = 'Nome da Rua'
time.sleep(0.8)
logradouro.clear()
logradouro.send_keys(a)
'======================================================================================================================'
# As linhas abaixo servem para selecionar uma opção do campo "Esse CEP é de:"
time.sleep(1)
select = Select(driver.find_element_by_name('tipoCEP'))
select.select_by_index(0)
time.sleep(2)
select.select_by_visible_text('Localidade/Logradouro')
'======================================================================================================================'
# Buscando o CEP digitado
time.sleep(1)
driver.find_element_by_id('btn_pesquisar').click()
time.sleep(1)


#Funções para validar se a consulta foi realizada conforme o esperado
def menorQue2carac():
    try:
        mensagem = driver.find_element_by_class_name('msg')
        if mensagem.is_enabled() or mensagem.is_enabled():
            print('O logradouro informado possui menos de 2 caracteres')
    except NoSuchElementException:
        time.sleep(1)


def msg_resultado():
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


'======================================================================================================================'

#Essa variável é sobre a mensagem apresentada quando o endereço informado possui menos de dois caracteres
menosDe2 = driver.find_element_by_name('')
#Essa variável é sobre a mensagem apresentada quando o endereço é consultado corretamente
elemento = driver.find_element_by_id('mensagem-resultado')
#Essa variável é sobre a mensagem apresentada quando o endereço informado está incorreto
elemento_erro = driver.find_element_by_class_name('mensagem')

'======================================================================================================================'

#Se o endereço informado possuir menos de 2 caracteres, então cairá nessa condição
if menosDe2.is_displayed() or menosDe2.is_enabled():
    menorQue2carac()

#Se o endereço informado for correto, então cairá nessa condição
if elemento.is_displayed() or elemento.is_enabled():
    msg_resultado()

#Se o endereço informado for incorreto, então cairá nessa condição
elif elemento_erro.is_enabled() or elemento_erro.is_displayed():
    msg_error()
