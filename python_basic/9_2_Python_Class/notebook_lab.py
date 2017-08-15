# 노트와 노트북 클래스 만들기 예제

class Note(object):
    def __init__(self, content = None):
        self.content = content

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = ""

    def __str__(self):
        return self.content


class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page=0):
        if self.page_number < 300:
            self.notes[self.page_number] = note
            self.page_number += 1
        else:
            self.notes = {page : note}
            self.page_number += 1

    def remove_note(self, page_number):
        if page_number in self.Note.Keys():
            return self.Note.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def get_number_of_page(self):
        return self.page_number

    def get_note(self):
        for index in range(1,self.page_number):
            print(index, self.notes[index])
