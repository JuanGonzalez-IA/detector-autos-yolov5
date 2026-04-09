# 🚗 Detector de Autos con Visión Artificial

Este es mi primer proyecto de visión artificial, donde desarrollé un modelo capaz de detectar autos utilizando YOLOv5.

## 🎥 Video de Demostracion = "demo.mp4"


## 🧠 Sobre el proyecto
El modelo fue entrenado con un dataset completamente creado por mí (imágenes + etiquetas manuales).

## 🔧 Tecnologías
- Python
- OpenCV
- PyTorch
- YOLOv5
- Google Colab
- Phycharm (uso local)

---

## 💻 Uso en tiempo real (cámara)

Archivo: `detect.py`

Permite detectar autos en tiempo real utilizando la cámara de la PC.

```bash
python detect.py

☁️ Uso en videos (Google Colab)

Notebook: colab/detector.ipynb

Permite procesar videos y descargarlos utilizando GPU para mejorar el rendimiento.

📦 Modelo

Descargar desde:
https://drive.google.com/file/d/1_k11hfoChNFZrLsSV42SMJVvkP3H6LnO/view?usp=sharing

Colocar en:
model/auto.pt

📊 Dataset

Dataset completamente creado por mí:

Imágenes propias
Labels manuales