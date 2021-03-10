from selenium import webdriver
from selenium.webdriver.support.ui import Select #a utilização deste método é viável para selecionar um determinado valor ou uma opção que fica dentro de um dropdown list
import time


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')


#Digitando o endereço no campo "Digite um CEP ou um Endereço:"
logradouro = driver.find_element_by_id('endereco')
#logradouro.send_keys('Rua Antonio Rogerio da Silva Rosa')
a = 'a'
logradouro.send_keys(a)


# As linhas abaixo servem para selecionar uma opção do campo "Esse CEP é de:"
time.sleep(1)
select = Select(driver.find_element_by_name('tipoCEP'))
select.select_by_index(0)
time.sleep(2)
select.select_by_visible_text('Localidade/Logradouro')


#Buscando o CEP digitado
time.sleep(1)
driver.find_element_by_id('btn_pesquisar').click()

try:
    #Se o endereço informado não cumprir com os requisitos, o código vai cair neste bloco try
    #Onde será realizado um novo processo de consulta 

    time.sleep(1)
    msg_alerta = driver.find_element_by_class_name('msg')
    if msg_alerta.is_enabled() or msg_alerta.is_displayed():
        print('O endereço informando possui menos de dois caracteres ou está incorreto')
        time.sleep(1)
        driver.refresh()

        b = str(input('Informe um novo nome de rua: '))
        #Se o logradouro informado possuir menos de dois caracteres, novamente será apresentado uma mensagem e novegador será fechado (não pensei em nada melhor a ser feito)
        if len(b) < 2:
            print('O logradouro  possui menos de 2 caracteres')
            driver.quit()
        else:
            #Senão, dessa vez será possível efetuar a consulta
            time.sleep(1)
            logradouro = driver.find_element_by_id('endereco')
            logradouro.send_keys(b)
            time.sleep(1)
            driver.find_element_by_id('btn_pesquisar').click()

        

except:
    print('Não funcionou')
    time.sleep(2)





'''
Isso tudo aqui em baixo é lixo

try:
    time.sleep(1)
    msg_alerta = driver.find_element_by_class_name('msg')
    if msg_alerta.is_enabled() or msg_alerta.is_displayed():
        driver.refresh()

except:
    print('Não funcionou')
    time.sleep(5)
    driver.quit()
'''
