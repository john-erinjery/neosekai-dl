import bs4
import os
from pickle import dump, load
import requests
import codecs
from neosekai_api import Novel, NovelChapter
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=13)


def download_chapter(_url):
    nc = NovelChapter(_url)
    if os.path.exists('content.txt'):
        pass
    else:
        open('content.txt', 'w', encoding='utf-8')
    with open('content.txt', 'a', encoding='utf-8') as f:
        print('downloading..' + nc.name)
        contents = nc.get_chapter_content()
        for i in contents:
            if contents[i]['type'] != 'img':
                try:
                    f.write(contents[i]['content'] + '\n')
                except:
                    print('error while writing ripping off one line :',
                          contents[i]['content'])


download_chapter(
    'https://www.neosekaitranslations.com/novel/please-tell-me-how-to-remember-love/volume-1/chapter-3-part-5/')
# def split_at_words_(line, num):
#     splitted_line = line.split()
#     line_list = []
#     temp_line = ''
#     count = 0
#     if len(line) <= num:
#         return [line]
#     ns = 0
#     ne = 0
#     indexes = []
#     for i in splitted_line:
#         count += len(i) + 1
#         ne += 1
#         if count >= num:
#             indexes.append([ns, ne])
#             ns = ne
#             count = len(i)
#         else:
#             pass
#     for i in indexes:
#         for j in splitted_line[i[0]:i[1]]:
#             temp_line += j + ' '
#         line_list.append(temp_line)
#         temp_line = ''
#     for i in splitted_line[ns:]:
#         temp_line += i + ' '
#     line_list.append(temp_line)
#     return line_list

# def text_to_pdf_converter(file, name):
#     for i in file:
#         lines = split_at_words_(i, 100)
#         for j in lines:
#             pdf.cell(300, 7, txt=j, ln = 1, align = 'L')
#     pdf.output(name + '.pdf')
