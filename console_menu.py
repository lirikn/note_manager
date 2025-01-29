# Интерактивное консольное меню

def main_menu():

    while True:
        print("\n=== Меню управления заметками ===")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("До свидания!")
            exit()
        else:
            print("Ошибка: Введите номер от 1 до 5.")

# Заглушки для функций

def add_note():
    print("Добавление заметки.")

def view_notes():
    print("Просмотр заметок.")

def edit_note():
    print("Редактирование заметки.")

def delete_note():
    print("Удаление заметки.")

if __name__ == "__main__":
    main_menu()

