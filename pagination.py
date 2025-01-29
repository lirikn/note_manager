# Постраничный вывод заметок с возможностью перехода между страницами

def display_page(notes, page, notes_per_page=3):
    start = (page - 1) * notes_per_page
    end = start + notes_per_page
    page_notes = notes[start:end]

    print(f"\n=== Страница {page} ===")
    for note in page_notes:
        print(f"{note['title']} ({note['status']}) — {note['created_date']}")

def paginate_notes(notes):
    page = 1
    notes_per_page = 3
    total_pages = (len(notes) + notes_per_page - 1) // notes_per_page

    while True:
        display_page(notes, page, notes_per_page)
        choice = input("\n[N] Следующая | [P] Предыдущая | [Q] Выход: ").strip().lower()

        if choice == "n" and page < total_pages:
            page += 1
        elif choice == "p" and page > 1:
            page -= 1
        elif choice == "q":
            break
        else:
            print("Ошибка: Некорректный выбор.")

if __name__ == "__main__":
    import json
    with open('notes_data.json', encoding='utf-8') as file:
        notes = json.load(file)
    paginate_notes(notes)

