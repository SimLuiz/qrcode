# Gerador de QR Code com Python

Este projeto é um script simples em Python para gerar QR Codes a partir de um link. O QR Code gerado pode ser utilizado para facilitar o acesso a sites, sistemas, formulários ou qualquer outro conteúdo online.

## 🔧 Requisitos

- Python 3.x instalado
- Biblioteca `qrcode` com suporte à imagem (PIL)

## 📦 Instalação

1. Clone este repositório ou baixe o arquivo `gerador_qrcode.py`
2. Instale a biblioteca necessária executando no terminal:

```bash
pip install qrcode[pil]

▶️ Como usar
Abra o arquivo gerador_qrcode.py

Substitua o valor da variável link pelo endereço desejado:

python
Copiar
Editar
link = "https://github.com/SimLuiz"
Salve o arquivo e execute no terminal:

bash
Copiar
Editar
python gerador_qrcode.py
Um arquivo de imagem qrcode_garantias.png será gerado na mesma pasta do script.

🧠 Observações
Certifique-se de não nomear o arquivo como qrcode.py, para evitar conflitos com a biblioteca instalada.

O QR Code gerado é estático e não expira, desde que o link continue válido.

Pode ser usado em sistemas, apresentações, documentos, etiquetas ou até impresso.

📁 Estrutura do Projeto
Copiar
Editar
qrcode/
├── gerador_qrcode.py
├── qrcode_garantias.png
└── README.md
💡 Exemplo de uso
O script pode ser utilizado, por exemplo, para gerar QR Codes que apontam para o sistema de garantias de baterias, facilitando o acesso rápido ao sistema via celular.

🧑‍💻 Autor
Luiz Felipe Moraes
Bacharel em Sistemas de Informação – IESGO
Desenvolvedor Web e Analista de BI
