import cv2
import torch
import pathlib

#para error PosixPath (Windows)
pathlib.PosixPath = pathlib.WindowsPath

# 🚀 Cargar modelo
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='C:/Users/juany/Desktop/Video/model/auto.pt',
                       force_reload=False)

# 🎯 Ajustes de precisión
model.conf = 0.7   # confianza mínima (subí/bajá entre 0.6–0.8)
model.iou = 0.45   # overlap entre cajas
model.max_det = 10 # máximo de detecciones por frame

# 🎥 Cámara (más compatible en Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ⚡ Resolución más liviana
WIDTH = 640
HEIGHT = 480

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ⚡ Redimensionar para mejorar FPS
    frame = cv2.resize(frame, (WIDTH, HEIGHT))

    # 🔍 Inferencia
    results = model(frame)

    # 🖼️ Render
    frame_render = results.render()[0]

    # 📺 Mostrar
    cv2.imshow('Detector de autos', frame_render)

    # ⛔ Salir con ESC
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()