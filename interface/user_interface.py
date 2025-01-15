# Функции взаимодействия с пользователем.
#from datetime import datetime, timedelta
from utils import *
from data import save_notes_to_file, load_notes_from_file, append_notes_to_file


# Функция отображения заметок.
def display_notes(notes):
    if not notes:
        print('Заметки не найдены.')
        return
    print('Список заметок: ')
    print('------------------------')
    for num, note in enumerate(notes, 1):
        print('\t\tЗаметка №', num)
        print('Имя пользователя:', note['username'])
        print('Заголовок:', note['title'])
        print('Описание:', note['content'])
        print('Статус:', note['status'])
        print('Дата создания:', note['created_date'])
        print('Дедлайн:', note['issue_date'])
        print('------------------------')
     # вывод 5 заметок на станице
        if not num % 5:
            input('Ввод для продолжения')

# Функция для создания новой заметки и возврата словаря.
def create_note():
    def input_check(text):
        while not (ret := input(f'Введите {text}: ')):
            print('Ввод не может быть пустым')
        return ret

    def input_status():
        while True:
            status = input('Введите статус заметки (новая, в процессе, выполнено): ')
            if validate_status(status):
                return status
            print('Неправильный статус -', status)

    def input_date(days):
        default = datetime.now() + timedelta(days=days)
        while True:
            if not (date := input(f'Введите дату дедлайна (по умолчанию {default.strftime("%d-%m-%Y")}):')):
                return default
            if date := validate_date(date):
                if date > datetime.now():
                    return date
                print('Дедлайн истек! Введите другую дату.')
            else:
                print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')

    return {
        'username': input_check('имя пользователя'),
        'title': input_check('заголовок заметки'),
        'content': input_check('описание заметки'),
        'status': input_status(),
        'created_date': datetime.now().strftime('%d-%m-%Y'),
        'issue_date': input_date(7).strftime('%d-%m-%Y'),
        'uuid': generate_unique_id()
    }

# Позволяет пользователю вносить изменения в уже созданные заметки, сохраняя их актуальность.
def update_note(note):
    print('Текущие данные заметки:\n', note)
    keys = ('username', 'title', 'content', 'status', 'issue_date')
    input_keys = ''
    while not input_keys:
        input_keys = input(f"Какие данные вы хотите обновить? ({', '.join(keys)}): ").split(', ')
        for key in input_keys:
            if key not in keys:
                print(f'некорректное имя поля {key}')
                input_keys = ''
                break
    for key in input_keys:
        # Пустой ввод не меняет содержимого поля
        if new := input(f'Введите новое значение для {key}: '):
            if key == 'issue_date':
                while not validate_date(new):
                    new = input(f'неправильный формат даты {new}, введите заново дд-мм-гггг: ')
            note[key] = new
    print('Заметка обновлена:\n', note)
    return note

# Функция поиска заметок
def search_notes(notes, keyword='', status=''):
    ret_notes = []
    if keyword:
        for note in notes:
            if [x for x in ('username', 'title', 'content') if keyword.lower() in note[x].lower()]:
                ret_notes.append(note)
        notes = ret_notes
    if status:
        ret_notes = []
        for note in notes:
            if status == note['status']:
                ret_notes.append(note)
    return ret_notes

# Меню для работы с заметками.
def select_note(notes, text):
    if notes:
        display_notes(notes)
        index = int(input(f'Введите номер заметки для {text}: ')) - 1
        if 0 <= index < len(notes):
            return index
        print("Неверный номер заметки.")
    else:
        print("Список заметок пуст.")
    return

def input_filename():
    if filename := input('Введите имя файла (по умолчанию - notes.txt): '):
        return filename
    return 'notes.txt'

def menu(notes):
    while True:
        print("""
            Меню действий:
            1. Создать новую заметку
            2. Показать все заметки
            3. Обновить заметку
            4. Удалить заметку
            5. Найти заметки
            6. Сохранить заметки в файл
            7. Добавить заметки в файл
            8. Загрузить заметки из файла
            9. Выйти из программы
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
            save_notes_to_file(notes, input_filename())
        elif choice == "7":
            append_notes_to_file(notes, input_filename())
        elif choice == "8":
            notes = load_notes_from_file(input_filename())
        elif choice == "9":
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    return notes
