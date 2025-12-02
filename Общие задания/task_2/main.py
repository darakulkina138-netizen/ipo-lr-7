#Вариант 2 - Кулькина
import json
def find_skill_by_code():
    # Чтение данных из файла
    try:
        with open('dump.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл dump.json не найден!")
        return
    except json.JSONDecodeError:
        print("Ошибка чтения JSON файла!")
        return
    # Ввод номера квалификации
    skill_code = input("Введите номер квалификации: ").strip()
    # Поиск квалификации
    found_skill = None
    for item in data:
        if item.get('model') == 'data.skill' and item.get('fields', {}).get('code') == skill_code:
            found_skill = item
            break
    # Вывод результата
    if found_skill:
        skill_fields = found_skill['fields']
        skill_title = skill_fields['title']
        # Поиск специальности для этой квалификации
        specialty_id = skill_fields['specialty']
        specialty_code = ""
        specialty_name = ""
        specialty_type = ""
        for item in data:
            if (item.get('model') == 'data.specialty' and 
                item.get('pk') == specialty_id):
                specialty_fields = item['fields']
                specialty_code = specialty_fields['code']
                specialty_name = specialty_fields['title']
                specialty_type = specialty_fields['c_type']
                break
        print("=============== Найдено ===============")
        print(f"{specialty_code} >> Специальность \"{specialty_name}\", {specialty_type}")
        print(f"{skill_code} >> Квалификация \"{skill_title}\"")
    else:
        print("=============== Не найдено ===============")

# Запуск программы
if __name__ == "__main__":
    find_skill_by_code()
