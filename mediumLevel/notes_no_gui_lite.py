import json

FILENAME = "notes.json"

try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        notes = json.load(f)
except:
    notes = []

while True:
    print("\nМеню:")
    print("1. Показать заметки")
    print("2. Добавить заметку")
    print("3. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        if notes:
            for i, note in enumerate(notes, 1):
                print(f"{i}.{note}")
        else:
            print("Пока нет заметок.")
    elif choice == "2":
        text = input("Введите текст заметки: ")
        notes.append(text)
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        print("Заметка сохранена!")
    elif choice == "3":
        break
    else:
        print("Неверный выбор")
