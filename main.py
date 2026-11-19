# Importar as bibliotecas 
import cv2
import numpy as np
from mpvc import DetectorMaos
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Captura da webcam
cap = cv2.VideoCapture(0)

# Instanciar o detector
detector = DetectorMaos(max_maos=1, deteccao_confianca=0.7)

# Obter o volume dos speakers
aparelhos = AudioUtilities.GetSpeakers()
volume = aparelhos.EndpointVolume

while True:
    # Obter a imagem capturada
    _, imagem = cap.read()

    # Detectar as mãos
    imagem = detector.encontrar_maos(imagem)

    # Obter a distância entre os pontos
    distancia, imagem, _ = detector.encontrar_distancia_pontos(4,8, imagem)

    # Converter a distância para o intervalo do volume
    vol = np.interp(
        distancia,
        [20,160],
        [0,1]
    )

    # Alterar o volume
    volume.SetMasterVolumeLevelScalar(vol, None)

    # Mostrar a imagem 
    cv2.imshow('Captura', imagem)

    # Delay de captura
    cv2.waitKey(1)
