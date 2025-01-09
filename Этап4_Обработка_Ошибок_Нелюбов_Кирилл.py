# Функция чтения заметок из файла.

def load_notes_from_file(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            info = file.readlines()
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as file:
            pass
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
    print(load_notes_from_file('notes.txt'))
