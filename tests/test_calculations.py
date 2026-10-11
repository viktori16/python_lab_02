import pytest
from app.calculations import create_body, calculate_all

def test_create_body_valid():
    body = create_body("1", [2, 3, 4], "сталь")
    assert body.name == "Параллелепипед"
    
    body = create_body("2", [5], "алюминий")
    assert body.name == "Тетраэдр"
    
    body = create_body("3", [1.5], "дерево")
    assert body.name == "Шар"

def test_create_body_invalid():
    with pytest.raises(ValueError, match="Неверный тип фигуры"):
        create_body("99", [1], "сталь")
        
    with pytest.raises(ValueError, match="Неизвестный материал"):
        create_body("1", [1, 1, 1], "золото")

def test_calculate_all():
    body = create_body("1", [2, 2, 2], "сталь")
    results = calculate_all(body)
    
    assert results["Название"] == "Параллелепипед"
    assert results["Объем (м^3)"] == 8.0
    assert results["Площадь поверхности (м^2)"] == 24.0
    assert results["Масса (кг)"] == 8.0 * 7800