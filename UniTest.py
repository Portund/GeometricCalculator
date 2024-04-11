import unittest, area_calculator


class TestCircleShape(unittest.TestCase):
    def test_areaCircle(self):
        circle = area_calculator.Circle(5)

class TestTriangleShape(unittest.TestCase):
    def test_areaTriangle(self):
        triangele = area_calculator.Triangle(3,4,5)

if __name__ == "__main__":
  unittest.main()      