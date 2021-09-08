import fitz  # this is pymupdf

filename = r'D:\PythonProject\dictionary_project\Malgudi Days.pdf'
filename2 = r'D:\PythonProject\dictionary_project\I Too Had a Love Story.pdf'
filename3 = r'D:\PythonProject\dictionary_project\Dharmayoddha Kalki _ Avatar of Vishnu.pdf'
filename4 = r'D:\PythonProject\dictionary_project\Digital Electronics And Logic Design.pdf'

# with fitz.open(r'D:\PythonProject\dictionary_project\Malgudi Days.pdf') as doc:
#     text = ""
#     for page in doc:
#         text += page.getText()

# print(text)

doc = fitz.open(filename3)     # or fitz.Document(filename)
# page = doc.load_page(pno)  # loads page number 'pno' of the document (0-based)
# page = doc[pno]  # the short form

print(doc.page_count)
# for numofPage in range(doc.page_count):
#     page = doc[numofPage]
#     print(page.getText())
page = doc[61]
print(page.getText())

# for page in doc:
#     # do something with 'page'

# # ... or read backwards
# for page in reversed(doc):
#     # do something with 'page'
# # ... or even use 'slicing'
# for page in doc.pages(start, stop, step):
#     # do something with 'page'