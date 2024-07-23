from docx import Document

def create_wf(text, filename = 'test.docx'):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)

if __name__ == "__main__":
    user_text = input("Введите текст для ворд файла: ")
    create_wf(user_text)
    print("Поздравляю файл создан")