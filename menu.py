# Меню для работы с заметками.
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from search_notes_function import search_notes

def select_note(notes, text):
    if notes:
        display_notes(notes)
        index = int(input(f'Введите номер заметки для {text}: ')) - 1
        if 0 <= index < len(notes):
            return index
        else:
            print("Неверный номер заметки.")
    else:
        print("Список заметок пуст.")
    return None

def menu(notes):
    while True:
        print("""
            Меню действий:
            1. Создать новую заметку
            2. Показать все заметки
            3. Обновить заметку
            4. Удалить заметку
            5. Найти заметки
            6. Выйти из программы
            """)
        choice = input("Ваш выбор: ")
        if choice == "1":
            notes.append(create_note())
        elif choice == "2":
            display_notes(notes)
        elif choice == "3":
            index = select_note(notes, 'обновления')
            if index is not None:
                notes[index] = update_note(notes[index])
        elif choice == "4":
            index = select_note(notes, 'удаления')
            if index is not None:
                del notes[index]
        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска (или оставьте пустым): ")
            status = input("Введите статус для поиска (или оставьте пустым): ")
            found_notes = search_notes(notes, keyword, status)
            display_notes(found_notes)
        elif choice == "6":
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    return notes

if __name__ == "__main__":
    notes_ = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
#    notes_ = []
    print('Добро пожаловать в "Менеджер заметок"!')
    menu(notes_)
