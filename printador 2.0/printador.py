import cv2
import numpy as np
import pyautogui
import time

# Número máximo de páginas
n_pag = 60

# Offset para tirar o texto vermelho
# use 18 ara monitor 1920x1080 a 75% e 31 para Ajustar à Janela
offset = 31

def detectar_folha_a4(imagem):
    """Detecta a região da folha branca (A4) na captura de tela."""
    img_cv = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos:
        return None

    contorno = max(contornos, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(contorno)

    if w < 500 or h < 700:
        return None
    return x, y, w, h

def capturar_paginas_auto(max_folhas=n_pag):
    """Captura as folhas automaticamente, rolando a página após cada uma."""
    print("🖥️ Captura automática iniciada!")
    print("Por favor, abra o PDF e deixe a primeira página visível...")
    time.sleep(5)

    max_tentativas = 5
    cont_folhas = 0
    falhas = 0

    while cont_folhas < max_folhas:
        screenshot = pyautogui.screenshot(allScreens=True)
        area = detectar_folha_a4(screenshot)

        if area:
            x, y, w, h = area
            folha = screenshot.crop((x + offset, y, x + w, y + h))

            nome_arquivo = f"folha_{cont_folhas + 1:03d}.png"
            folha.save(nome_arquivo, optimize=False, compress_level=0)

            cont_folhas += 1
            falhas = 0
            print(f"✅ Folha {cont_folhas} salva ({nome_arquivo})")

            
            print("↘️ Rolando para próxima página...")
            # Rola para próxima página. Coloque em 75% de zoom em um monitor 1920x1080
            # pyautogui.scroll(-1023)  # valor negativo = rolar para baixo
            # Coloque na opção "Ajustar à Janela"
            pyautogui.press('down')
            time.sleep(0.1)

        else:
            falhas += 1
            print(f"⚠️ Nenhuma folha detectada ({falhas}/5 tentativas)...")
            if falhas >= max_tentativas:
                print("🏁 Fim do documento detectado. Captura encerrada.")
                break
            time.sleep(2)


if __name__ == "__main__":
    capturar_paginas_auto()
