# Функции для работы с файлами.
import json
from utils import generate_unique_id

def save_notes_to_file(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("--------\n")
    except PermissionError:
        print(f'Отсутствуют права доступа к файлу {filename}')

def load_notes_from_file(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            info = file.readlines()
    except FileNotFoundError:
        open(filename, 'w').close()
        print(f'Файл {filename} не найден. Создан новый файл.')
        return []
    except UnicodeDecodeError:
        print(f'Ошибка при чтении файла {filename}. Проверьте его содержимое.')
        return
    except PermissionError:
        print(f'Отсутствуют права доступа к файлу {filename}')
        return
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    repl = {'Имя пользователя': 'username',
            'Заголовок': 'title',
            'Описание': 'content',
            'Статус': 'status',
            'Дата создания': 'created_date',
            'Дедлайн': 'issue_date'}
    notes = []
    note = {}
    for line in info:
        line = line.replace('\n', '').split(': ')
        if line == ['--------']:
            notes.append(note)
            note = {}
        else:
            note[repl[line[0]]] = line[1]
            note['uuid'] = generate_unique_id()
    return notes

def append_notes_to_file(notes, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("--------\n")

def save_notes_json(notes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

def load_notes_json(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            return json.load(file)
    except:
        return []
