# Функция чтения заметок из файла.
from save_to_file_function import save_notes_to_file, notes_

def load_notes_from_file(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            info = file.readlines()
    except FileNotFoundError:
        save_notes_to_file(notes_, filename)
        print(f'Файл {filename} не найден. Создан новый файл.')
        return
    except UnicodeDecodeError:
        print(f'Ошибка при чтении файла {filename}. Проверьте его содержимое.')
        return
    except PermissionError:
        print(f'Отсутствуют права доступа к файлу {filename}')
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
    return notes

if __name__ == "__main__":
    notes = load_notes_from_file('notes.txt')
    print(notes)
