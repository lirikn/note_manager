# Позволяет пользователю вносить изменения в уже созданные заметки, сохраняя их актуальность.
from datetime import datetime

# Функция позволяет вводить несколько полей для изменения, возвращает список.
def input_check():
    keys = ('username', 'title', 'content', 'status', 'issue_date')
    input_keys = input(f"Какие данные вы хотите обновить? ({', '.join(keys)}): ").split(', ')
    for key in input_keys:
        if key not in keys:
            print(f'некорректное имя поля {key}')
            return
    return input_keys

def date_check(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except:
        return False
    return True

def update_note(note):
    print('Текущие данные заметки:\n', note)
    input_keys = input_check()
    while input_keys is None:
        input_keys = input_check()
    for key in input_keys:
        new = input(f'Введите новое значение для {key}: ')
        # Пустой ввод не меняет содержимого поля
        if new != '':
            if key == 'issue_date':
                while not date_check(new):
                    new = input(f'неправильный формат даты {new}, введите заново дд-мм-гггг: ')
            note[key] = new
    print('Заметка обновлена:\n', note)
    return note

if __name__ == "__main__":
    note_ = {'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'}
    note_ = update_note(note_)
