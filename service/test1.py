from docx import Document

doc = Document('test.docx')
full_text = []
for i in doc.paragraphs:
    full_text.append(i.text)

print(full_text)