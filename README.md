Este desafio consiste em automatizar o download de arquivos PDF de um site e compactá-los em um único arquivo .zip.
A aplicação deve acessar o site do gov.br/ANS, localizar os Anexos I e II em formato PDF e armazená-los corretamente.

## Etapas Executadas
1️⃣ Acessar a URL da ANS via requests.
2️⃣ Extrair os links dos PDFs usando BeautifulSoup.
3️⃣ Baixar os arquivos PDF e salvar localmente.
4️⃣ Compactar os arquivos gerando um .zip chamado Anexos.zip.

## Tecnologias Utilizadas
- requests → Para acessar e baixar os arquivos
- BeautifulSoup → Para encontrar os links dentro da página
- zipfile → Para compactação dos PDFs

# Transformação de dados 

1️⃣ Extrair dados do PDF do Anexo I usando PyMuPDF.
2️⃣ Converter os dados para um arquivo CSV usando pandas.
3️⃣ Corrigir abreviações ("OD" → "Odontologia", "AMB" → "Ambulatorial").
4️⃣ Compactar o arquivo CSV gerando um .zip chamado Teste_Mari.zip.

## Tecnologias Utilizadas
- PyMuPDF (fitz) → Para leitura do PDF
- pandas → Para organização dos dados
- zipfile → Para compactação do CSV

