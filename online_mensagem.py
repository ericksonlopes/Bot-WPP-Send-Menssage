from selenium import webdriver
import time
from datetime import datetime

# o driver que ser[a usado
drive = webdriver.Chrome('chromedriver.exe')

# o site da execução
drive.get('https://web.whatsapp.com/')

# tempo necessário para ler o QR
time.sleep(15)

contato = 'Ana Claúdia'

# procura pela conversa com o nome da conversa ou número
btn_nome = drive.find_element_by_xpath(f"//span[@title='{contato}']")
time.sleep(2)
# clica na conversa
btn_nome.click()

while True:
    try:
        # caminho do span com o titulo de 'online' e 'digitando'
        status = '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span'
        time.sleep(0.30)
        status = drive.find_element_by_xpath(status)
    # caso ele não encontre significa que o usuario está online
    except :
        print('O usuario não esta online')
    else:
        # se o objeto for encontrado, verifica se o texto dentro
        time.sleep(10)
        if status.text == 'clique aqui para dados do contato':
            print('O usuario não esta online')
        elif status.text == 'online' or 'digitando':
            # status da pessoa online/digitando
            print(status.text, '-> Enviar mensagem!')
            # procura a caixa de texto na página
            caixa_texto = drive.find_element_by_class_name('_1Plpp')
            time.sleep(0.30)
            # Coloca dentro do texto encontrado a frase dentro dos parenteses
            caixa_texto.send_keys('ACABOU')
            time.sleep(0.30)
            # procura o botão que envia mensagem
            btn_enviar = drive.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(0.30)
            # clia no botão e envia a mensagem
            btn_enviar.click()



