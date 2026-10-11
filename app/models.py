import math
from abc import ABC, abstractmethod

class GeometricBody(ABC):
    """Абстрактный базовый класс для всех геометрических тел."""
    
    def __init__(self, name: str, material: str):
        self._name = name
        self._material = material

    # Managed-атрибуты (свойства)
    @property
    def name(self) -> str:
        return self._name

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Материал должен быть непустой строкой")
        self._material = value.lower()

    # Абстрактные методы
    @abstractmethod
    def volume(self) -> float:
        """Расчет объема."""
        pass

    @abstractmethod
    def surface_area(self) -> float:
        """Расчет площади поверхности."""
        pass

    def mass(self, density: float) -> float:
        """Расчет массы: Объем * Плотность."""
        return self.volume() * density

    # Dunder-методы
    def __str__(self) -> str:
        return f"{self.name} из материала '{self.material}'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', material='{self.material}')"


class Parallelepiped(GeometricBody):
    def __init__(self, a: float, b: float, c: float, material: str):
        super().__init__("Параллелепипед", material)
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._a = value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._b = value

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._c = value

    def volume(self) -> float:
        return self._a * self._b * self._c

    def surface_area(self) -> float:
        return 2 * (self._a * self._b + self._b * self._c + self._a * self._c)

    def __str__(self) -> str:
        return f"{super().__str__()} (a={self._a}, b={self._b}, c={self._c})"

    def __repr__(self) -> str:
        return f"Parallelepiped(a={self._a}, b={self._b}, c={self._c}, material='{self.material}')"


class Tetrahedron(GeometricBody):
    def __init__(self, edge: float, material: str):
        super().__init__("Тетраэдр", material)
        self.edge = edge

    @property
    def edge(self) -> float:
        return self._edge

    @edge.setter
    def edge(self, value: float):
        if value <= 0:
            raise ValueError("Длина ребра должна быть положительной")
        self._edge = value

    def volume(self) -> float:
        return (self._edge ** 3) / (6 * math.sqrt(2))

    def surface_area(self) -> float:
        return math.sqrt(3) * (self._edge ** 2)

    def __str__(self) -> str:
        return f"{super().__str__()} (ребро={self._edge})"

    def __repr__(self) -> str:
        return f"Tetrahedron(edge={self._edge}, material='{self.material}')"


class Sphere(GeometricBody):
    def __init__(self, radius: float, material: str):
        super().__init__("Шар", material)
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value

    def volume(self) -> float:
        return (4 / 3) * math.pi * (self._radius ** 3)

    def surface_area(self) -> float:
        return 4 * math.pi * (self._radius ** 2)

    def __str__(self) -> str:
        return f"{super().__str__()} (радиус={self._radius})"

    def __repr__(self) -> str:
        return f"Sphere(radius={self._radius}, material='{self.material}')"