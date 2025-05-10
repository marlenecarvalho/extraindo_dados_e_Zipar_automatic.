import requests
from bs4 import BeautifulSoup
import zipfile
import unicodedata
import fitz
import pandas as pd

# url da página que você deseja fazer o scraping
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
#acessar o site
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#procurar links para os PDFs
pdf_links = []
for link in soup.find_all('a', href=True):
    if 'pdf' in link['href']:
        pdf_links.append(link['href'])

# Baixar os PDFs
for idx, pdf_url in enumerate(pdf_links):
    pdf_response = requests.get(pdf_url)
    with open(f"Anexo_{idx+1}.pdf", "wb") as pdf_file:
        pdf_file.write(pdf_response.content)

import fitz  # PyMuPDF
import pandas as pd

# Abrindo o PDF
pdf_path = "Anexo_2.pdf"
doc = fitz.open(pdf_path)

# Lista para armazenar os dados extraídos
tabela_dados = []

# Percorrer todas as páginas do PDF
for page in doc:
    blocks = page.get_text("blocks")  # Extrai blocos de texto

    for b in blocks:
        linha = b[4]  # O texto extraído está na posição 4 do bloco
        tabela_dados.append(linha.split("\t"))  # Divide colunas

# Criar DataFrame
df = pd.DataFrame(tabela_dados)

print(df.head())  # Exibir amostra dos dados

#salvar em arquivo CSV
#corrigir erros de acentuação e ç 
def normalizar_texto(texto):
    return unicodedata.normalize("NFKD", texto)

# Aplicando a função em todas as colunas do DataFrame
df = df.applymap(normalizar_texto)
texto_corrigido = normalizar_texto("ação, médico, público")


df.to_csv("Rol_Procedimentos.csv", index=False, encoding='UTF-8')
print("Texto corrigido!")  # Agora está correto!
print("dados salvos em CSV!")

substituicoes = {
    "OD" : "ODONTOLOGIA",
    "AMB" : "AMBULATORIAL"
}

df.replace(substituicoes, inplace=True)
df.to_csv("Rol_procedimentos_Modificados.csv", index=False, encoding='UTF-8')
print("Abreviações substituídas!")

#compactar o arquivo CSV e Zip
zipfile_name = "Teste1_substituicoes{Marlene_Carvalho}.zip"
text = page.get_text("text").encode("UTF-8").decode("UTF-8")
with zipfile.ZipFile(zipfile_name, 'w') as zipf:
    zipf.write("Rol_Procedimentos_Modificados.csv")
    print(f"Arquivo compactado: {zipfile_name}")



print("Download completed.")

#compactar em arquivo zip
zipfile_name = "Anexos.zip"

with zipfile.ZipFile(zipfile_name, 'w') as zipf:
    zipf.write("Anexo_1.pdf")
    zipf.write("Anexo_2.pdf")

print(f"Arquivos compactados em {zipfile_name}")


