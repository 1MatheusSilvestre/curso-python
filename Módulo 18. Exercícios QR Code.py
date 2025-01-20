import qrcode 
from qrcode.image.styledpil import StyledPilImage  

# Cria uma instância do QRCode com um nível de correção de erro alto
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  

# Adiciona a URL do canal do YouTube ao QR code
qr.add_data("https://www.youtube.com/@HashtagProgramacao")  

# Cria a imagem do QR code, usando uma imagem incorporada (logo) e a classe StyledPilImage
imagem = qr.make_image(
    image_factory=StyledPilImage,  # Define o estilo da imagem
    embeded_image_path="logo.png",  # Caminho da imagem que será incorporada ao QR code
)

# Salva a imagem gerada como 'qrcode_logo.png'
imagem.save("qrcode_logo.png")  

# Dicionário contendo links das redes sociais
redes_sociais = {
  "Facebook": "https://www.facebook.com/hashtagprogramacao",
  "Instagram": "https://www.instagram.com/hashtagprogramacao",
  "YouTube": "https://www.youtube.com/@HashtagProgramacao",
  "TikTok": "https://www.tiktok.com/@hashtagprogramacao",
}

# Loop através de cada rede social e seu respectivo URL
for rede_social, url in redes_sociais.items():
  # Cria uma nova instância do QRCode para cada rede social com correção de erro alta
  qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  
  # Adiciona o URL da rede social ao QR code
  qr.add_data(url)  

  # Cria a imagem do QR code para a rede social, usando a mesma imagem incorporada
  imagem = qr.make_image(
      image_factory=StyledPilImage,  
      embeded_image_path="logo.png",  
  )

  # Salva a imagem gerada com um nome baseado na rede social (ex: sociais_Facebook.png)
  imagem.save(f"sociais_{rede_social}.png")  
