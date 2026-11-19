# Importar as bibliotecas 
import cv2
import numpy as np
from mpvc import DetectorMaos
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Captura da webcam
cap = cv2.VideoCapture(0)

# Instanciar o detector
detector = DetectorMaos(max_maos=1, deteccao_confianca=0.7)

while True:
    # Obter a imagem capturada
    _, imagem = cap.read()

    # Detectar as mãos
    imagem = detector.encontrar_maos(imagem)

    # Mostrar a imagem 
    cv2.imshow('Captura', imagem)

    # Delay de captura
    cv2.waitKey(1)
