from app.calculations import create_body, calculate_all, MATERIALS_DENSITY
from app.reporting import save_to_xlsx, save_to_docx
from app.database import init_db, save_calculation, get_history

def main():
    # Инициализируем базу данных при запуске
    init_db()
    
    while True:
        print("\n=== Расчет геометрических тел (Вариант 16) ===")
        print("1. Параллелепипед")
        print("2. Тетраэдр")
        print("3. Шар")
        print("4. Показать историю расчетов")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "0":
            print("Выход из программы.")
            break
            
        if choice == "4":
            history = get_history()
            if not history:
                print("\nИстория пуста.")
            else:
                print("\n=== История расчетов ===")
                for row in history:
                    print(f"[{row[0]}] {row[1]} ({row[2]}) -> {row[3]}")
            continue
            
        if choice in ["1", "2", "3"]:
            params = {}
            if choice == "1":
                params['a'] = float(input("Введите длину a: "))
                params['b'] = float(input("Введите ширину b: "))
                params['c'] = float(input("Введите высоту c: "))
            elif choice == "2":
                params['edge'] = float(input("Введите длину ребра: "))
            elif choice == "3":
                params['radius'] = float(input("Введите радиус: "))

            print(f"\nДоступные материалы: {', '.join(MATERIALS_DENSITY.keys())}")
            material = input("Введите материал: ").lower()
            params['material'] = material

            try:
                body = create_body(choice, list(params.values())[:-1], material)
                results = calculate_all(body)
                
                print("\n=== Результаты расчета ===")
                for key, value in results.items():
                    print(f"{key}: {value}")
                
                # Сохраняем в БД автоматически
                save_calculation(results, params)
                
                save_choice = input("\nСохранить отчет в файл? (y/n): ").lower()
                if save_choice == 'y':
                    format_choice = input("Выберите формат (1 - Excel, 2 - Word): ")
                    if format_choice == "1":
                        save_to_xlsx(results)
                    elif format_choice == "2":
                        save_to_docx(results)
                    else:
                        print("Неверный формат.")
                        
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()