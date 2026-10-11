import sqlite3
import json
from datetime import datetime

DB_NAME = "calculations.db"

def init_db():
    """Создает таблицу для хранения истории расчетов, если её нет."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            shape_name TEXT NOT NULL,
            material TEXT NOT NULL,
            params TEXT NOT NULL,
            results TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_calculation(data: dict, params: dict):
    """Сохраняет результат расчета в базу данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    shape_name = data.get("Название", "Неизвестно")
    material = data.get("Материал", "Неизвестно")
    
    # Преобразуем словари в строки JSON для хранения в БД
    params_json = json.dumps(params, ensure_ascii=False)
    results_json = json.dumps(data, ensure_ascii=False)
    
    cursor.execute('''
        INSERT INTO history (timestamp, shape_name, material, params, results)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, shape_name, material, params_json, results_json))
    
    conn.commit()
    conn.close()
    print("Результат успешно сохранен в базу данных!")

def get_history():
    """Возвращает историю всех расчетов."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, shape_name, material, results FROM history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows