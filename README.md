# Sistema Automático de Mensagens no WhatsApp

Projeto em Python para envio automático de mensagens personalizadas no WhatsApp utilizando uma tabela CSV com nomes e números.

---

## Funcionalidades

* Leitura automática de contatos via CSV
* Mensagens personalizadas com o nome de cada pessoa
* Integração com WhatsApp Web
* Envio automático de mensagens utilizando Python

---

## Tecnologias utilizadas

* Python
* pandas
* pywhatkit

---

## Instalação

### 1. Clone o repositório

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

---

### 2. Instale as dependências

Antes de executar o projeto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

---

## Configuração do arquivo CSV

O projeto utiliza um arquivo `.csv` contendo os contatos.

Crie um arquivo CSV seguindo este modelo:

| nome  | numero        | tipo    |
| ----- | ------------- | ------- |
| João  | 5583987654321 | dourado |
| Maria | 5583999999999 | padrão  |

### Regras importantes

* O arquivo CSV deve conter as colunas:

```text
nome
numero
tipo
```

* Os números devem estar no formato:

```text
55 + DDD + número
```

Exemplo:

```text
5583987654321
```

* Não utilize:

  * espaços
  * parênteses
  * hífens
  * sinal de +

---

## Configurando o caminho do CSV

No código Python, altere o caminho do arquivo CSV para o caminho do seu arquivo:

```python
pd.read_csv("SEU_ARQUIVO.csv")
```

Exemplo:

```python
pd.read_csv("contatos.csv")
```

---

## Como executar

1. Deixe o WhatsApp Web logado no navegador
2. Execute o script Python:

```bash
python sistemaMensagens.py
```

---

## Observações importantes

* Teste primeiro utilizando seu próprio número
* Evite envios muito rápidos para não correr risco de bloqueio no WhatsApp
* Não feche o navegador durante o envio automático
* Dependendo da internet, talvez seja necessário aumentar o `wait_time`

---

## Exemplo de mensagem personalizada

```python
mensagem = f"Opa {nome}! Aqui é da Panini e seu Album de capa dura {tipo} já chegou em nossa loja, venha buscar o quanto antes!!"
```

---

## Licença

Projeto desenvolvido para fins de estudo e automação pessoal.
