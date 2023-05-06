import extractor
import os
from prettytable import PrettyTable
from neosekai_api import Novel

novel = Novel(input('Enter novel URL : '))
print("detecting chapters...")
index = novel.get_index_page()
data = [["index", "name", "volume"]]
for i in index:
    ch_name_full = index[i]["chapter_name"]
    ch = ch_name_full if ch_name_full == index[i]["chapter_name"][:
                                                                  21] else index[i]["chapter_name"][:21] + '..'
    index_no = i
    volume = index[i]["volume"]
    data.append([index_no, ch, volume])
table = PrettyTable()
table.left_padding_width = 1
table.right_padding_width = 1
table.field_names = data[0]
for i in range(1, len(data)):
    table.add_row(data[i])
print(table)

link_dict = {}
for i in index:
    link_dict[i] = index[i]['url']

range__ = eval(input('\nenter range : '))
for i in range(range__[0], range__[1] + 1):
    extractor.download_chapter(link_dict[str(i)])
print('\nconverting to PDF..')
extractor.text_to_pdf_converter(open('content.txt', 'r', encoding='utf-8',
                                errors='ignore'), str(str(range__[0]) + '-' + str(range__[1])))
print('\ndeleting content.txt and cache..')
os.remove('content.txt')
print('done!')
