import pandas as pd
import time
import pywhatkit as kit 
data = pd.read_csv("NomeDeSuaTabelaCSV") # Coloque aqui o nome do seu arquivo CSV(ele precisa está na mesma pasta deste código)

# percorrer csv linha por linha salvando nome e numero do cliente
for i,linha in data.iterrows():
    nome = linha['nome']
    numero = f"+{linha['numero']}"

    mensagem = f"Opa {nome}! Aqui é da Panini e seu Album de capa dura já chegou em nossa loja, venha buscar o quanto antes!!"
    kit.sendwhatmsg_instantly(numero,mensagem,wait_time = 6,tab_close = True)

    time.sleep(10)
