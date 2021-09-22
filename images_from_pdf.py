import fitz

file_name = r'D:\PythonProject\dictionary_project\I Too Had a Love Story.pdf'
path = r'D:\PythonProject\dictionary_project\data\images\books\itohadalovestory'

pdf = fitz.open(file_name)
no_of_pages = pdf.page_count

for page_number in range(no_of_pages):
    image_list = pdf.getPageImageList(page_number)
    for image in image_list:
        xref = image[0]
        pix = fitz.Pixmap(pdf, xref)
        if pix.n < 5:
            pix.writePNG(f'{path}\{xref}.png')
        else:
            pix1 = fitz.open(fitz.csRGB, pix)
            pix1.writePNG(f'{path}\{xref}.png') # D:\PythonProject\dictionary_project\data\images\books\aghora\
            pix1 = None
        pix = None
    print(f'{page_number}/{no_of_pages} detected')
    # print(len(image_list), f'detected in page number {page_number}')

