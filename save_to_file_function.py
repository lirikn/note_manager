# Функция записи заметок в файл
#import yaml

def save_notes_to_file(notes, filename):
    file = open(filename, 'w', encoding='utf-8')
#    file.write(yaml.dump(notes, allow_unicode=True, sort_keys=False))
    for note in notes:
        file.write(f"Имя пользователя: {note['username']}\n")
        file.write(f"Заголовок: {note['title']}\n")
        file.write(f"Описание: {note['content']}\n")
        file.write(f"Статус: {note['status']}\n")
        file.write(f"Дата создания: {note['created_date']}\n")
        file.write(f"Дедлайн: {note['issue_date']}\n")
        file.write("--------\n")
    file.close()

if __name__ == "__main__":
    notes_ = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
#    save_notes_to_file(notes_, 'notes.yaml')
    save_notes_to_file(notes_, 'notes.txt')