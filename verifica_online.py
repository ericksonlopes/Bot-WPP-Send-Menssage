from selenium import webdriver
import time

class wapbot:
    def __init__(self):
        # caminho do chromdriver
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        # URl que deseja abrir
        self.driver.get('https://web.whatsapp.com/')

        # tempo para logar
        time.sleep(15)

        pri = '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span'
        pri = f"//span[@title='Aiza']"

        pessoa = self.driver.find_element_by_xpath(pri)
        time.sleep(2)
        pessoa.click()
        time.sleep(3)

        while True:
            try:
                status = '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span'
                time.sleep(0.30)
                status = self.driver.find_element_by_xpath(status)
            except Exception as err:
                print('O usuario não esta online\n', err)
            else:
                if status.text == 'online':
                    print(status.text)
                else:
                    'A pessoa não esta online'


bot = wapbot()