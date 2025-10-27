import json
import os

FILENAME = "notes.json"

def load_notes():
    if not os.path.exists(FILENAME):
        # создаём пустой файл при первом запуске
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def show_notes(notes):
    if not notes:
        print("Пока тут пусто.")
        return
    print("\nСписок заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']}")
        print()

def create_note(notes):
    title = input("Введи название:")
    text = input("Введи содержимое:")
    note_id = max([n["id"] for n in notes], default=0) + 1
    notes.append({"id": note_id, "title": title, "text": text})
    save_notes(notes)
    print("Заметка сохранена.")

def view_note(notes):
    show_notes(notes)
    try:
        note_id = int(input("Введите номер заметки: "))
    except ValueError:
        print("Неверный ввод.")
        return
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        print(f"\n{note['title']}\n{'-' * len(note['title'])}")
        print(note['text'])
        print()
    else:
        print("Заметка не найдена.\n")

def edit_note(notes):
    show_notes(notes)
    try:
        note_id = int(input("Введите ID заметки для редактирования: "))
    except ValueError:
        print("Неверный ввод.\n")
        return
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        print("Заметка не найдена.\n")
        return

    print(f"\nРедактирование '{note['title']}'")
    new_title = input("Новое название (оставьте пустым, чтобы не менять): ")
    new_text = input("Новый текст (оставьте пустым, чтобы не менять): ")

    if new_title:
        note["title"] = new_title
    if new_text:
        note["text"] = new_text

    save_notes(notes)
    print("Заметка обновлена!\n")

def main():
    notes = load_notes()

    while True:
        print("=== Меню заметок ===")
        print("1. Показать все заметки")
        print("2. Создать новую заметку")
        print("3. Просмотреть заметку")
        print("4. Редактировать заметку")
        print("5. Выйти")

        choice = input("Выбери действие:")

        if choice == "1":
            print("Выбрано показать все заметки")
            show_notes(notes)
        elif choice == "2":
            print("Выбрано создать новую заметку")
            create_note(notes)
        elif choice == "3":
            print("Выбрано просмотреть заметку")
            view_note(notes)
        elif choice == "4":
            print("Выбрано редактировать заметку")
            edit_note(notes)
        elif choice == "5":
            print("Выбрано выйти")
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main()
