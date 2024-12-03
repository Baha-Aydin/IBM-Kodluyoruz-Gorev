import math

# 1. Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (2, 9)]

# 2. Öklid mesafesi için fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# 3. Mesafelerin hesaplanması
distances = []  # Mesafeleri saklamak için bir liste

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum mesafenin bulunması
min_distance = min(distances)
print("Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
