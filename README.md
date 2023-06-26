# Extrator de Links

Um simples programa em Python para extrair links de uma página da web.

## Funcionalidades

- Permite inserir um link para uma página da web.
- Extrai os links encontrados na página.
- Salva os primeiros 10 links em um arquivo de saída.

## Requisitos

- Python 3.x
- Bibliotecas: requests, bs4 (BeautifulSoup)

## Como usar

1. Faça o download do arquivo extrator_de_links.py para o seu ambiente local.
2. Certifique-se de ter os requisitos mencionados instalados em seu ambiente Python.
3. Abra o terminal ou prompt de comando e navegue até o diretório em que o arquivo extrator_de_links.py está localizado.
4. Execute o seguinte comando:

```
python extrator_de_links.py
```

5. Será solicitado que você digite o link da página da web a ser analisada. Insira o link e pressione Enter.
6. O programa irá extrair os links encontrados na página e salvar os primeiros 10 links em um arquivo chamado "meusLinks.txt" no mesmo diretório do script.
7. Você pode abrir o arquivo "meusLinks.txt" para visualizar os links extraídos.

Certifique-se de que o link fornecido comece com "http://" ou "https://". Se você não incluir o prefixo "http://" ou "https://", o programa adicionará automaticamente "https://" antes do link fornecido.

## Personalização

- Para alterar o número de links salvos no arquivo de saída, você pode modificar a linha `print(links[:10], file=arquivo_salvo)` e especificar o número desejado.
- Se você preferir sobrescrever o arquivo de saída em vez de anexar os links a cada execução, altere o modo de abertura do arquivo de "a" (append) para "w" (write) na linha `with open("meusLinks.txt", 'a') as arquivo_salvo`.
 
