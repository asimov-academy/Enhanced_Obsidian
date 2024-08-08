import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from langflow.load import run_flow_from_json

class Isaac:
    api_key = "OPENAI_API_KEY"
    dir_path = os.getcwd()
    options = webdriver.ChromeOptions()
    profile = os.path.join(dir_path, "profile", "wpp")
    options.add_argument(
        r"user-data-dir={}".format(profile)
    )
    # options.add_argument("--headless=new")
    webdriver = webdriver.Chrome(options=options)
    webdriver.get("https://web.whatsapp.com")
    sleep(155)

    try:
        caixa_de_pesquisa = webdriver.find_element(By.XPATH, (
            '//button[@aria-label="Pesquisar ou começar uma nova conversa"]'
            )
        )
        caixa_de_pesquisa.click()
        caixa_de_pesquisa.send_keys('I.S.A.A.C.')
        sleep(2)
        contato = webdriver.find_element(By.XPATH, '//*[@title="I.S.A.A.C."]')
        contato.click()
    except Exception as e:
        raise e

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        try:
            post = self.webdriver.find_elements(By.CLASS_NAME, 'message-out')
            texto = post[-1].find_element(By.CLASS_NAME, 'selectable-text').text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!", e)

if __name__ == '__main__':
    bot = Isaac()
    msg = ''
    last_msg = '/quit'
    while msg != '/quit':
        sleep(1)
        msg = bot.ultima_msg()
        if msg != last_msg:
            last_msg = msg
            print(msg)
            try:
                result = run_flow_from_json(
                    flow="Note from youtube trasncript.json",
                    input_value=msg,
                )
            except Exception as e:
                print(e)



