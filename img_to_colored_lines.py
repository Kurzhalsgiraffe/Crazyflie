import cv2
import numpy as np
import matplotlib.pyplot as plt

colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray',
    'olive', 'cyan', 'magenta', 'gold', 'teal', 'navy', 'lime', 'maroon',
    'turquoise', 'darkgreen', 'coral', 'indigo'
]

# Bild laden
image_path = "albsig.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bild verkleinern
scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# Kanten erkennen
edges = cv2.Canny(resized, 50, 150)

# Konturen finden
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Plot vorbereiten
plt.figure(figsize=(8, 6))
plt.imshow(np.zeros_like(edges), cmap='gray')  # schwarzer Hintergrund

# Farben und Koordinaten ausgeben
for i, contour in enumerate(contours):
    color = colors[i % len(colors)]
    x_vals = []
    y_vals = []
    print(f"Pfad {i+1} ({color}):")
    for point in contour:
        x, y = point[0]
        x_vals.append(x)
        y_vals.append(y)
        print(f"X{x} Y{y}")
    plt.plot(x_vals, y_vals, color=color, linewidth=1)

plt.title("Konturen in verschiedenen Farben")
plt.axis('off')
plt.show()
