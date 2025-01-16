# Тесты для проверки функций.
import unittest
from data import save_notes_to_file, load_notes_from_file

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [{
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
        }]
        save_notes_to_file(notes, 'test_notes.txt')
        loaded_notes = load_notes_from_file('test_notes.txt')
        self.assertEqual(notes, loaded_notes)

if __name__ == '__main__':

    unittest.main()