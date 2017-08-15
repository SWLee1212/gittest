from notebook_lab import Note
from notebook_lab import NoteBook

MyNoteBook = NoteBook("The Exam Book")

new_note = Note()
new_note.write_content("This is for test. Python is the most simple language.")
MyNoteBook.add_note(new_note)

MyNoteBook.add_note(Note("Hello word !!"))
MyNoteBook.add_note(Note("Hello word !!"))
MyNoteBook.add_note(Note("Hello word !!"))
MyNoteBook.add_note(Note("Hello word !!"))
MyNoteBook.add_note(Note("Hello word !!"))

MyNoteBook.get_note()
