import os
from neosekai_api import NovelChapter
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=13)


def download_chapter(_url):
    nc = NovelChapter(_url)
    name = nc.chapter_details(name_only=True)
    print('downloading and processing..' + name)
    if os.path.exists('content.txt'):
        pass
    else:
        open('content.txt', 'w', encoding='utf-8')

    with open('content.txt', 'a', encoding='utf-8') as f:
        f.write('\n\n' + name + '\n\n')
        contents = nc.get_chapter_content(fancy=False)
        for i in contents:
            if contents[i]['type'] != 'img':
                try:
                    f.write(contents[i]['content'] + '\n')
                except:
                    print('error while writing.. ripping off one line :',
                          contents[i]['content'], sep='\n')


def split_at_words_(line, num):
    splitted_line = line.split()
    line_list = []
    temp_line = ''
    count = 0
    if len(line) <= num:
        return [line]
    ns = 0
    ne = 0
    indexes = []
    for i in splitted_line:
        count += len(i) + 1
        ne += 1
        if count >= num:
            indexes.append([ns, ne])
            ns = ne
            count = len(i)
        else:
            pass
    for i in indexes:
        for j in splitted_line[i[0]:i[1]]:
            temp_line += j + ' '
        line_list.append(temp_line)
        temp_line = ''
    for i in splitted_line[ns:]:
        temp_line += i + ' '
    line_list.append(temp_line)
    return line_list


def text_to_pdf_converter(file, name):
    for i in file:
        lines = split_at_words_(i, 100)
        for j in lines:
            pdf.cell(300, 7, txt=j, ln=1, align='L')
    pdf.output(name + '.pdf')
