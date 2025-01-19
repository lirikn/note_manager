# Тесты для проверки функций.
import unittest
from data import save_notes_to_file, load_notes_from_file
from utils import *
from interface import display_notes

notes = [{
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'
}]

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        save_notes_to_file(notes, 'test_notes.txt')
        loaded_notes = load_notes_from_file('test_notes.txt')
        self.assertEqual(notes, loaded_notes)

    def test_date_format(self):
        date = '20-21-2025'
        ret = validate_date(date)
        self.assertEqual(ret, None)

    def test_status(self):
        status = 'в процессе'
        ret = validate_status(status)
        self.assertEqual(ret, True)

    def test_display_notes(self):
        display_notes(notes)

    def test_generate_unique_id(self):
        uuid = generate_unique_id()
        print(uuid)

if __name__ == '__main__':

    unittest.main()