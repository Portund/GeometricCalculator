import area_calculator


circle = area_calculator.Circle(5) 
triangle = area_calculator.Triangle(3, 4, 5)

print(f'Площадь круга с радиусом 5: {circle.area()}')

print(f'Площадь треугольника со сторонами 3,4,5: {triangle.area()}')

print('Треугольник со сторонами 3,4,5 прямоугольный') if triangle.is_right_angled()  \
else print('Треугольник со сторонами 3,4,5 не прямоугольный')

