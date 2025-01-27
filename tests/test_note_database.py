# Тесты для проверки функций.
import unittest
from database.note_operations import *

note = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'
}

id_ = 0

class TestNoteManager(unittest.TestCase):
    def test1_save_and_load_notes(self):
        global id_
        create_note_db('notes.db')
        save_note_to_db(note, 'notes.db')
        loaded_note = load_notes_from_db('notes.db')[-1]
        id_ = loaded_note.pop('id')
        self.assertEqual(note, loaded_note)

    def test2_update_note_in_db(self):
        updates = {'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'выполнена', 'issue_date': '02-12-2024'}
        update_note_in_db(id_, updates, 'notes.db')
        loaded_notes = load_notes_from_db('notes.db')
        for note_ in loaded_notes:
            if note_.pop('id') == id_:
                self.assertNotEqual(note_, note)
                break

    def test3_search_notes_by_keyword(self):
        notes = search_notes_by_keyword('продукты', 'notes.db')
        self.assertTrue(notes)
        notes = search_notes_by_keyword('чёрти-что', 'notes.db')
        self.assertFalse(notes)

    def test4_filter_notes_by_status(self):
        notes = filter_notes_by_status('выполнена', 'notes.db')
        self.assertTrue(notes)
        notes = filter_notes_by_status('новая', 'notes.db')
        self.assertFalse(notes)

    def test5_delete_note_from_db(self):
        delete_note_from_db(id_, 'notes.db')
        loaded_notes = load_notes_from_db('notes.db')
        self.assertFalse([x for x in loaded_notes if x['id'] == id_])

if __name__ == '__main__':
    unittest.main()