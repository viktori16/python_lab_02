import pytest
import math
from app.models import Parallelepiped, Tetrahedron, Sphere

def test_parallelepiped_calculations():
    p = Parallelepiped(2, 3, 4, "сталь")
    assert p.volume() == 24
    assert p.surface_area() == 52
    assert p.mass(7800) == 24 * 7800
    assert str(p) == "Параллелепипед из материала 'сталь' (a=2, b=3, c=4)"
    assert "Parallelepiped" in repr(p)

def test_tetrahedron_calculations():
    t = Tetrahedron(2, "дерево")
    expected_volume = (2 ** 3) / (6 * math.sqrt(2))
    assert math.isclose(t.volume(), expected_volume, rel_tol=1e-9)
    expected_area = math.sqrt(3) * (2 ** 2)
    assert math.isclose(t.surface_area(), expected_area, rel_tol=1e-9)

def test_sphere_calculations():
    s = Sphere(1, "пластик")
    assert math.isclose(s.volume(), (4/3) * math.pi, rel_tol=1e-9)
    assert math.isclose(s.surface_area(), 4 * math.pi, rel_tol=1e-9)

def test_managed_attributes_validation():
    with pytest.raises(ValueError, match="Длина должна быть положительной"):
        Parallelepiped(-1, 2, 3, "сталь")
    
    with pytest.raises(ValueError, match="Радиус должен быть положительным"):
        Sphere(0, "дерево")

    p = Parallelepiped(1, 1, 1, "сталь")
    with pytest.raises(ValueError, match="Материал должен быть непустой строкой"):
        p.material = ""