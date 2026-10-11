from app.models import Parallelepiped, Tetrahedron, Sphere

# Справочник плотностей материалов (кг/м^3)
MATERIALS_DENSITY = {
    "сталь": 7800,
    "алюминий": 2700,
    "дерево": 700,
    "пластик": 1200
}

def create_body(shape_type: str, params: list, material: str):
    """Фабрика для создания объектов геометрических тел."""
    if material not in MATERIALS_DENSITY:
        raise ValueError(f"Неизвестный материал: {material}")
    
    if shape_type == "1": # Параллелепипед
        return Parallelepiped(params[0], params[1], params[2], material)
    elif shape_type == "2": # Тетраэдр
        return Tetrahedron(params[0], material)
    elif shape_type == "3": # Шар
        return Sphere(params[0], material)
    else:
        raise ValueError("Неверный тип фигуры")

def calculate_all(body):
    """Выполняет все расчеты для тела."""
    density = MATERIALS_DENSITY[body.material]
    return {
        "Название": body.name,
        "Материал": body.material,
        "Объем (м^3)": round(body.volume(), 4),
        "Площадь поверхности (м^2)": round(body.surface_area(), 4),
        "Масса (кг)": round(body.mass(density), 4)
    }