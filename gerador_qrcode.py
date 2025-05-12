import qrcode

# Link para o QR Code
link = "https://github.com/SimLuiz"

# Gerar o QR Code
qr = qrcode.make(link)
# Salvar como imagem

qr.save("qrcode_garantias.png")
# Exibir o QR Code

