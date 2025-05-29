import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('persona.jpg')

# Verificar si la imagen se cargó
if imagen is None:
    print("Error: No se pudo cargar la imagen...")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque para eliminar ruido
gris_suave = cv2.medianBlur(gris, 7)

bordes = cv2.adaptiveThreshold(gris_suave, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 9, 10)

color = cv2.bilateralFilter(imagen, d=9, sigmaColor=250, sigmaSpace=250)
comic = cv2.bitwise_and(color, color, mask=bordes)

# Añadir texto
cv2.putText(comic, 'Filtro Comic', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Mostrar imágenes
cv2.imshow('Original', imagen)
cv2.imshow('Comic', comic)

# Guardar imagen
cv2.imwrite('persona_comic.jpg', comic)
print("Imagen guardada como 'persona_comic.jpg'")


cv2.waitKey(0)
cv2.destroyAllWindows()
