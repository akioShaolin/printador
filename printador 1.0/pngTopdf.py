from PIL import Image
import os

# Caminho onde estão as imagens
pasta_imagens = r"C:\Users\pedro.sakuma\OneDrive - EcoPower Energia Solar\Área de Trabalho\printador"

# Filtra todos os arquivos .png da pasta
arquivos = [f for f in os.listdir(pasta_imagens) if f.lower().endswith('.png')]

# Ordena os arquivos pelo nome (importante se forem folha_001.png, folha_002.png, etc.)
arquivos.sort()

# Lista para armazenar as imagens abertas
imagens = []

for arquivo in arquivos:
    caminho = os.path.join(pasta_imagens, arquivo)
    img = Image.open(caminho).convert('RGB')  # garante formato RGB
    imagens.append(img)

# Gera o PDF com todas as imagens
if imagens:
    pdf_saida = os.path.join(pasta_imagens, "documento_final.pdf")
    imagens[0].save(pdf_saida, save_all=True, append_images=imagens[1:])
    print(f"✅ PDF criado com sucesso: {pdf_saida}")
else:
    print("⚠️ Nenhuma imagem PNG encontrada na pasta.")
