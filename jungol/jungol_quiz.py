#####  Quiz. 삼각형과 사각형의 무게 중심을 구하는 프로그램을 작성하시오.

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def get_centroid(self):
        n = len(self.vertices)
        sum_x = sum(v[0] for v in self.vertices)
        sum_y = sum(v[1] for v in self.vertices)
        return (round(sum_x / n, 2), round(sum_y / n, 2))

triangle = Polygon([(0, 0), (10, 0), (5, 10)])
quadrilateral = Polygon([(0, 0), (8, 0), (8, 8), (0, 8)])

print(f"삼각형 무게 중심: {triangle.get_centroid()}")
print(f"사각형 무게 중심: {quadrilateral.get_centroid()}")

#################################################################(방법01)

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def get_centroid(self):
        n = len(self.vertices)
        sum_x = sum(v[0] for v in self.vertices)
        sum_y = sum(v[1] for v in self.vertices)
        return (round(sum_x / n, 2), round(sum_y / n, 2))

triangle = Polygon([(0, 0), (10, 0), (5, 10)])
quadrilateral = Polygon([(0, 0), (8, 0), (8, 8), (0, 8)])

print(f"삼각형 무게 중심: {triangle.get_centroid()}")
print(f"사각형 무게 중심: {quadrilateral.get_centroid()}")

#################################################################(방법02)

