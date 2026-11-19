# 🎚️ Controle de Volume por Gestos

Projeto desenvolvido em Python que permite controlar o volume do sistema utilizando gestos das mãos capturados pela webcam.

Através da biblioteca OpenCV e de um detector de mãos, o programa identifica a distância entre o polegar e o dedo indicador para ajustar o volume do computador em tempo real.

## 🚀 Funcionalidades

- 📷 Captura de vídeo em tempo real pela webcam.
- ✋ Detecção de mãos utilizando a biblioteca `mpvc`.
- 📏 Identificação da distância entre o polegar e o dedo indicador.
- 🔊 Controle do volume do sistema através de gestos.
- 📊 Barra visual que representa o nível do volume.
- 💯 Exibição da porcentagem atual do volume.

## 🛠️ Tecnologias utilizadas

- **Python** — Linguagem de programação.
- **OpenCV** — Captura e processamento de imagens.
- **NumPy** — Interpolação dos valores de distância e volume.
- **MPVC** — Detecção e rastreamento das mãos.
- **PyCAW** — Controle do volume de áudio do Windows.

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Instale as dependências

```bash
pip install opencv-python numpy pycaw comtypes
```

Instale também a biblioteca `mpvc`, conforme o método de instalação disponibilizado pelo projeto que fornece esse módulo.

## ▶️ Como executar

Execute o arquivo principal:

```bash
python main.py
```

Certifique-se de que sua webcam esteja conectada e funcionando.

## 🖐️ Como funciona

O funcionamento do projeto é baseado na distância entre dois pontos da mão:

- **Ponto 4:** ponta do polegar.
- **Ponto 8:** ponta do dedo indicador.

O programa calcula a distância entre esses dois pontos e utiliza a função `numpy.interp()` para converter essa distância em um valor de volume entre 0 e 100%.

| Distância entre os dedos | Volume |
|---|---|
| 20 pixels | 0% |
| 90 pixels | Aproximadamente 50% |
| 160 pixels | 100% |

A interface também apresenta uma barra visual que acompanha o nível do volume em tempo real.

## ⌨️ Controles

- Aproxime os dedos para diminuir o volume.
- Afaste os dedos para aumentar o volume.
- Pressione `Q` para encerrar o programa.

## ⚙️ Requisitos

- Python 3 instalado.
- Webcam funcionando.
- Sistema operacional Windows (necessário para o controle de áudio com PyCAW).
- Dependências instaladas.


## 👨‍💻 Autor

Projeto desenvolvido como prática de estudos em Python, visão computacional e automação utilizando gestos das mãos.
