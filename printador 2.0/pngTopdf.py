import os
import img2pdf
from PIL import Image
import shutil

# Caminho onde estão as imagens
pasta_imagens = r"C:\\Users\\pedro.sakuma\\OneDrive - EcoPower Energia Solar\\Área de Trabalho\\printador\\printador 2.0"

# Cria uma subpasta temporária para as versões JPEG
pasta_temp = os.path.join(pasta_imagens, "temp_jpg")
os.makedirs(pasta_temp, exist_ok=True)

# Filtra e ordena os arquivos PNG
arquivos = sorted([f for f in os.listdir(pasta_imagens) if f.lower().endswith('.png')])

caminhos_jpeg = []

print("🧩 Convertendo imagens para JPEG (com compressão leve)...")

for arquivo in arquivos:
    caminho_png = os.path.join(pasta_imagens, arquivo)
    nome_jpg = os.path.splitext(arquivo)[0] + ".jpg"
    caminho_jpg = os.path.join(pasta_temp, nome_jpg)

    # Abre e converte
    img = Image.open(caminho_png).convert("RGB")
    img.save(caminho_jpg, quality=85, optimize=True)  # ajuste 'quality' entre 60 e 95

    caminhos_jpeg.append(caminho_jpg)

# Gera o PDF
pdf_saida = os.path.join(pasta_imagens, "documento_final.pdf")

if caminhos_jpeg:
    with open(pdf_saida, "wb") as f:
        f.write(img2pdf.convert(caminhos_jpeg))
    print(f"✅ PDF comprimido criado com sucesso: {pdf_saida}")
else:
    print("⚠️ Nenhuma imagem PNG encontrada na pasta.")

# 🧹 Deleta todas as imagens originais e a pasta temporária
for arquivo in arquivos:
    os.remove(os.path.join(pasta_imagens, arquivo))
#shutil.rmtree(pasta_temp)

print("🧹 Todas as imagens foram removidas após a conversão.")