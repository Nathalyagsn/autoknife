import pyautogui
import numpy as np
import time
import cv2


def find_red_circle(frame):
    # Converter a imagem para HSV (para facilitar a detecção de cor)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Faixa de cor vermelha (ajuste se necessário)
    lower_red1 = np.array([0, 120, 70])    # Tons mais escuros de vermelho
    upper_red1 = np.array([10, 255, 255])  # Tons mais claros de vermelho
    lower_red2 = np.array([170, 120, 70])  # Tons mais escuros de vermelho (faixa complementar)
    upper_red2 = np.array([180, 255, 255])  # Tons mais claros de vermelho (faixa complementar)

    # Máscaras para vermelho
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Aplicar a máscara na imagem original
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Converter para escala de cinza (necessário para detectar círculos)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Detectar círculos usando HoughCircles
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,  # Precisão do acumulador
        minDist=50,  # Distância mínima entre círculos detectados
        param1=50,  # Parâmetro do detector de bordas Canny
        param2=30,  # Limite para detecção de círculo
        minRadius=10,  # Raio mínimo do círculo
        maxRadius=100  # Raio máximo do círculo
    )

    return circles


print("Preparando para começar...")
time.sleep(5)

while True:
    # Captura de tela
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Converter para o formato correto do OpenCV

    # Detectar o círculo vermelho
    circles = find_red_circle(frame)

    if circles is not None:
        # Converter as coordenadas do círculo para valores inteiros
        circles = np.uint16(np.around(circles))
        x, y, radius = circles[0, 0]
        
        # Garantir que o clique seja centralizado no círculo detectado
        center_x = int(x)  # Coordenada central X
        center_y = int(y)  # Coordenada central Y

        print(f"Clique na posição central do círculo: ({center_x}, {center_y})")

        # Clicar no centro do círculo
        pyautogui.click(center_x, center_y)

        
        time.sleep(3)
    else:
        print("Nenhum círculo vermelho encontrado. Aguardando...")
        time.sleep(3)  # Pausa maior quando nenhum círculo é encontrado
