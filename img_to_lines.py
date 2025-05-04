import cv2
import matplotlib.pyplot as plt

image_path = "albsig.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

edges = cv2.Canny(resized, threshold1=50, threshold2=150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

paths = []
for contour in contours:
    path = []
    for point in contour:
        x, y = point[0]
        path.append((x, y))
    paths.append(path)

for i, path in enumerate(paths):
    print(f"Pfad {i+1}:")
    for point in path:
        print(f"X{point[0]} Y{point[1]}")

plt.imshow(edges, cmap='gray')
plt.title("Gefundene Kanten")
plt.show()
