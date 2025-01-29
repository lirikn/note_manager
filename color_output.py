# Цветовое выделение заметок в зависимости от их статуса

from colorama import Fore, Style

def display_notes_with_colors(notes):
    print("\n=== Список заметок ===")
    for note in notes:
        if note['status'] == 'Важная':
            print(Fore.RED + f"• {note['title']}" + Style.RESET_ALL)
        elif note['status'] == 'Выполненная':
            print(Fore.GREEN + f"• {note['title']}" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + f"• {note['title']}" + Style.RESET_ALL)


if __name__ == "__main__":
    import json
    with open('notes_data.json', encoding='utf-8') as file:
        notes = json.load(file)

    display_notes_with_colors(notes)

