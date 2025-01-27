# Главная программа, запускающая проект.
from interface import menu
from data import save_notes_json, load_notes_json

save_notes = 'notes.json'

notes = load_notes_json(save_notes)
menu(notes)
save_notes_json(notes, save_notes)
