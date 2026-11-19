
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
    sucesso, imagem = cap.read()

    if not sucesso:
        break

    # Detectar as mãos
    imagem = detector.encontrar_maos(imagem)

    # Obter a distância entre os pontos
    distancia, imagem, _ = detector.encontrar_distancia_pontos(
        4, 8, imagem
    )

    # Converter a distância para o intervalo do volume
    vol = np.interp(
        distancia,
        [20, 160],
        [0, 1]
    )

    # Limitar o volume entre 0 e 100%
    vol = np.clip(vol, 0, 1)

    # Converter a distância para a altura da barra
    vol_barra = np.interp(
        distancia,
        [20, 160],
        [400, 100]
    )

    # Converter a distância para porcentagem
    vol_porc = np.interp(
        distancia,
        [20, 160],
        [0, 100]
    )

    # Limitar a porcentagem
    vol_porc = np.clip(vol_porc, 0, 100)

    # Barra externa do volume
    cv2.rectangle(
        imagem,
        (50, 100),
        (85, 400),
        (167, 59, 93),
        3
    )

    # Barra interna preenchida
    cv2.rectangle(
        imagem,
        (50, int(vol_barra)),
        (85, 400),
        (0, 255, 0),
        cv2.FILLED
    )

    # Mostrar a porcentagem do volume
    cv2.putText(
        imagem,
        f'{int(vol_porc)}%',
        (40, 450),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (0, 0, 255),
        3
    )

    # Alterar o volume do sistema
    volume.SetMasterVolumeLevelScalar(float(vol), None)

    # Mostrar a imagem
    cv2.imshow('Captura', imagem)

    # Encerrar ao pressionar Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a webcam e fechar as janelas
cap.release()
cv2.destroyAllWindows()
