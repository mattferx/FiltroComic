# 📚 Filtro Cómic con OpenCV

Este proyecto aplica un **filtro estilo cómic** a cualquier imagen utilizando Python y OpenCV. Convierte tus fotos en ilustraciones con contornos marcados y colores planos, simulando una historieta o caricatura digital.

## 🧠 ¿Cómo funciona?

El efecto se logra mediante:
- Conversión a escala de grises y desenfoque.
- Detección de bordes con umbral adaptativo.
- Suavizado de colores con un filtro bilateral.
- Combinación final de bordes y color para lograr el estilo cómic.

## 🚀 Requisitos

- Python 3.x
- OpenCV  
  Puedes instalarlo con:

  ```bash
  pip install opencv-python
▶️ Cómo usarlo
Asegúrate de tener una imagen llamada persona.jpg en la misma carpeta.

Ejecuta el script:

python filtro_comic.py
Se mostrará el resultado y se guardará una nueva imagen llamada persona_comic.jpg.

🛠 Archivos incluidos
filtro_comic.py – Código principal del filtro cómic.

persona.jpg – Imagen de prueba (puedes usar cualquier otra).
