import json


def find_company_data(data):
    result = []

    # Проверка, является ли переданный объект словарем
    if isinstance(data, dict):
        # Поиск ключей 'title' и 'id' в словаре
        title = data.get('title', None)
        company_id = data.get('id', None)

        # Если оба ключа присутствуют, добавляем данные в результат
        if title is not None and company_id is not None:
            result.append((title, company_id))

        # Рекурсивный обход значений словаря
        for value in data.values():
            result.extend(find_company_data(value))

    # Проверка, является ли переданный объект списком
    elif isinstance(data, list):
        # Рекурсивный обход элементов списка
        for item in data:
            result.extend(find_company_data(item))

    return result


def main():
    # Загрузка данных из файла JSON
    with open("../Recursive/new_test_hw.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)

    # Вызываем функцию для поиска данных о компаниях
    companies_data = find_company_data(json_data)

    # Вывод результата
    for company in companies_data:
        print(company)


if __name__ == "__main__":
    main()
