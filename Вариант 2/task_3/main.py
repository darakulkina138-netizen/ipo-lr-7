#Вариант 2 - Кулькина
import json
import os
FILE_NAME = "flowers.json"
operation_count = 0
if not os.path.exists(FILE_NAME):
    initial_data = [
        {"id": 1,
            "name": "Роза",
            "latin_name": "Rosa",
            "is_red_book_flower": False,
            "price": 10},
        {"id": 2,
            "name": "Тюльпан",
            "latin_name": "Tulipa",
            "is_red_book_flower": True,
            "price": 7},
        {"id": 3,
            "name": "Орхидея",
            "latin_name": "Orchidaceae",
            "is_red_book_flower": True,
            "price": 8},
        {"id": 4,
            "name": "Ландыш",
            "latin_name": "Convallaria majalis",
            "is_red_book_flower": True,
            "price": 5},
        {"id": 5,
            "name": "Ромашка",
            "latin_name": "Matricaria chamomilla",
            "is_red_book_flower": False,
            "price": 2}]
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=2)
    operation_count += 1
while True:
    print("\nМЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ О ЦВЕТАХ")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    try:
        choice = int(input("Выберите пункт меню (1-5): "))
    except ValueError:
        print("Ошибка! Введите число от 1 до 5")
        continue
    if choice == 1:
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                flowers = json.load(file)
            if not flowers:
                print("\nБаза данных пуста!")
            else:
                print("\nВСЕ ЗАПИСИ О ЦВЕТАХ:")
                for i, flower in enumerate(flowers, 1):
                    print(f"\nЗапись #{i}:")
                    print(f"  ID: {flower['id']}")
                    print(f"  Название: {flower['name']}")
                    print(f"  Латинское название: {flower['latin_name']}")
                    red_book_status = "Да" if flower['is_red_book_flower'] else "Нет"
                    print(f"  Краснокнижный: {red_book_status}")
                    print(f"  Цена: {flower['price']} руб.")
                operation_count += 1
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
    elif choice == 2:
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                flowers = json.load(file)
            try:
                search_id = int(input("Введите ID записи для поиска: "))
            except ValueError:
                print("Ошибка! ID должен быть числом")
                continue
            found = False
            for i, flower in enumerate(flowers):
                if flower["id"] == search_id:
                    print("\nНАЙДЕННАЯ ЗАПИСЬ:")
                    print(f"Позиция в списке: {i + 1}")
                    print(f"ID: {flower['id']}")
                    print(f"Название: {flower['name']}")
                    print(f"Латинское название: {flower['latin_name']}")
                    red_book_status = "Да" if flower['is_red_book_flower'] else "Нет"
                    print(f"Краснокнижный: {red_book_status}")
                    print(f"Цена: {flower['price']} руб.")
                    found = True
                    operation_count += 1
                    break
            if not found:
                print(f"\nЗапись с ID {search_id} не найдена!")
        except Exception as e:
            print(f"Ошибка: {e}")
    elif choice == 3:
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                flowers = json.load(file)
            if flowers:
                next_id = max(flower["id"] for flower in flowers) + 1
            else:
                next_id = 1
            print("\nДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ")
            new_flower = {"id": next_id}
            new_flower["name"] = input("Введите название цветка: ").strip()
            new_flower["latin_name"] = input("Введите латинское название: ").strip()
            red_book_input = input("Является ли краснокнижным? (да/нет): ").strip().lower()
            new_flower["is_red_book_flower"] = red_book_input in ["да", "yes", "y", "1", "true"]
            try:
                new_flower["price"] = float(input("Введите цену (руб.): "))
            except ValueError:
                print("Ошибка! Цена должна быть числом. Установлено значение 0")
                new_flower["price"] = 0
            flowers.append(new_flower)
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(flowers, file, ensure_ascii=False, indent=2)
            print(f"\nЗапись успешно добавлена с ID {next_id}!")
            operation_count += 1
        except Exception as e:
            print(f"Ошибка: {e}")
    elif choice == 4:
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                flowers = json.load(file)
            try:
                delete_id = int(input("Введите ID записи для удаления: "))
            except ValueError:
                print("Ошибка! ID должен быть числом")
                continue
            found = False
            for i, flower in enumerate(flowers):
                if flower["id"] == delete_id:
                    del flowers[i]
                    with open(FILE_NAME, "w", encoding="utf-8") as file:
                        json.dump(flowers, file, ensure_ascii=False, indent=2)
                    print(f"\nЗапись с ID {delete_id} успешно удалена!")
                    found = True
                    operation_count += 1
                    break
            if not found:
                print(f"\nЗапись с ID {delete_id} не найдена!")
        except Exception as e:
            print(f"Ошибка: {e}")
    elif choice == 5:
        print(f"\nКоличество выполненных операций: {operation_count}")
        print("Выход из программы.")
        break
    else:
        print("Ошибка! Выберите пункт от 1 до 5")
