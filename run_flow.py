import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from langflow.load import run_flow_from_json
from dotenv import load_dotenv

load_dotenv()

class Isaac:
    whats_group_name = 'I.S.A.A.C.' # nome do grupo do whats que você criou
    dir_path = os.getcwd()
    options = webdriver.ChromeOptions()
    profile = os.path.join(dir_path, "profile", "wpp")
    options.add_argument(
        r"user-data-dir={}".format(profile)
    )
    # options.add_argument("--headless=new") # Você deve loggar no whats web na primeira vez, depois pode descomentar esta linha
    webdriver = webdriver.Chrome(options=options)
    webdriver.get("https://web.whatsapp.com")
    sleep(155)

    try:
        caixa_de_pesquisa = webdriver.find_element(By.XPATH, (
            '//button[@aria-label="Pesquisar ou começar uma nova conversa"]'
            )
        )
        caixa_de_pesquisa.click()
        caixa_de_pesquisa.send_keys(f'{whats_group_name}')
        sleep(2)
        contato = webdriver.find_element(By.XPATH, f'//*[@title="{whats_group_name}"]')
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
    api_key=os.getenv("OPENAI_API_KEY") # crie um arquivo chamado .env onde registra sua OPENAI_API_KEY
    model_name = "gpt-4o-mini"  # Mantive a opção de alterar o modelo da OpenAI, porem nos meus testes a de melhor custo beneficio foi a 4o-mini.
    TWEAKS = {
        "TextInput-oysby": {
            "openai_api_key": api_key
        },
        # "OpenAIModel-Qpy4Z": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        # "OpenAIModel-I67FN": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        # "TextInput-I5Dkp": {
        #     "path": ""
        # },
        # "OpenAIModel-cuJuy": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        # "OpenAIModel-dZ7Hd": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        # "OpenAIModel-8WG98": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        # "OpenAIModel-4kwNZ": {
        #     "model_name": "gpt-4o-mini",
        #     "temperature": 0.1
        # },
        "TextInput-MtBsz": {
            "input_value": "/path/to/your/obsidian_folder"# caminho para a sua pasta no obsidian
        }
    }

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
                    fallback_to_env_vars=True,
                    tweaks=TWEAKS,
                )
            except Exception as e:
                print(e)



