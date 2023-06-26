import requests as rq
from bs4 import BeautifulSoup

url = input("Digite o link: ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Escrevendo a saída em um arquivo (meusLinks.txt) em vez de imprimir na saída padrão
# Você pode alterar 'a' para 'w' para sobrescrever o arquivo a cada vez
with open("meusLinks.txt", 'a') as arquivo_salvo:
    print(links[:10], file=arquivo_salvo)