import pyautogui
import numpy as np
import time

# Função para verificar se o pixel é vermelho
def is_red(pixel):
    r, g, b = pixel
    return r > 150 and g < 100 and b < 100  # Tons predominantes de vermelho

# Aguardar antes de iniciar
time.sleep(5)

while True:
    # Capturar a tela inteira
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)

    # Procurar pixels vermelhos de forma eficiente
    red_positions = np.argwhere((frame[:, :, 0] > 150) &  # R alto
                                 (frame[:, :, 1] < 100) &  # G baixo
                                 (frame[:, :, 2] < 100))   # B baixo

    if red_positions.size > 0:  # Se houver pixels vermelhos
        y, x = red_positions[0]  # Pegar o primeiro pixel encontrado
        pyautogui.click(x, y)    # Clicar no pixel
        print(f"Clique na posição: ({x}, {y})")
        time.sleep(0.5)  # Pequena pausa para evitar cliques contínuos
