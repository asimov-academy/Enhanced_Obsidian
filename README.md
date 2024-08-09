# Obsidian_Enhanced

Este projeto automatiza a criação de notas no Obsidian utilizando Inteligência Artificial para resumir partes de vídeos. A automação é feita utilizando um fluxo criado no Langflow que faz uso de agentes, PyTube, Whisper, e salva as notas geradas diretamente na pasta do Obsidian.

## Funcionalidades

* *Automatização de Resumos de Vídeos:* Captura e resume automaticamente vídeos de youtube utilizando IA.
* *Integração com WhatsApp Web:* A automação é acionada por mensagens recebidas em um grupo específico do WhatsApp.
* *Salvamento Automático no Obsidian:* As notas geradas são automaticamente salvas na pasta de referência do Obsidian.

## Tecnologias Utilizadas

* *Python 3.12*
* *Poetry* para gerenciamento de dependências
* *Langflow* para criação e execução do pipeline
* *PyTube* para download de vídeos do YouTube
* *Whisper* para transcrição de áudio
* *OpenAI GPT* para geração de resumos
* *Selenium* para automação do WhatsApp Web
* *Obsidian* como ferramenta de notas
* *dotenv* para gerenciamento de variáveis de ambiente

## Configuração

### Pré-requisitos

* Python 3.12
* Biblioteca dotenv para carregar as variáveis de ambiente
* Um arquivo .env contendo a sua chave da OpenAI API (OPENAI_API_KEY)
* Google Chrome instalado (para o Selenium)
* Um grupo criado no WhatsApp com um nome especificado no código
* [Poetry](https://python-poetry.org/docs/#installation) instalado

### Instalação e Configuração

1. *Clone este repositório:*

   bash
   git clone https://github.com/asimov-academy/Enhanced_Obsidian
   cd Enhanced_Obsidian
   

2. *Inicialize o Projeto com Poetry:*

   bash
   poetry init
   

   Siga as instruções para configurar o nome do projeto, versão, etc.

3. *Instale as Dependências:*

   Utilize o poetry para instalar as bibliotecas necessárias:

   bash
   poetry add selenium langflow openai whisper pytubefix python-dotenv
   

4. *Crie e Configure o Arquivo .env:*

   Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI API:

   plaintext
   OPENAI_API_KEY = 'sua-chave-aqui'
   

5. *Inicie o Projeto:*

   Ative o ambiente virtual com poetry e execute o projeto:

   bash
   poetry shell
   python -m langflow run
   python run_flow.py
   

   Isso ativará o ambiente, inicializará o langflow e executará o script principal.

### Execução

1. O Selenium abrirá o Google Chrome, e você deve se logar no WhatsApp Web na primeira execução.

2. Envie mensagens no grupo do WhatsApp configurado para iniciar a criação de notas. O projeto utilizará o Whisper para transcrever vídeos e gerar notas no Obsidian.

### Personalização

* O modelo OpenAI utilizado pode ser configurado nas TWEAKS.
* O grupo do WhatsApp e o nome da pasta do Obsidian podem ser alterados no script Python.
* O tempo de espera para o login do WhatsApp Web pode ser ajustado no script Python.

## Contribuições

Sinta-se à vontade para enviar issues ou pull requests. Contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a [Asimov Academy](LICENSE).