# Фильтрация заметок

def filter_notes(notes, filter_type, filter_value):
    if filter_type == "keyword":
        return [note for note in notes if filter_value.lower() in note['title'].lower()]
    elif filter_type == "status":
        return [note for note in notes if note['status'] == filter_value]
    elif filter_type == "date":
        return [note for note in notes if note['date'] == filter_value]
    else:
        return notes

