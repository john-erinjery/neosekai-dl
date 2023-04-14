import extractor
import os
link_dict, range_ = extractor.link_dat_file()
print(f'chapters {range_[0]} to {range_[1]} detected.')
range__ = eval(input('\nenter range : '))
for i in range(range__[0], range__[1] + 1):
    print('\ndownloading and processing chapter..', i)
    extractor.download_chapter_with_url(link_dict[i], i)
print('\nconverting to PDF..')
extractor.text_to_pdf_converter(open('content.txt', 'r', encoding='utf-8', errors='ignore'), str(str(range__[0]) + '-' + str(range__[1])))
print('\ndeleting content.txt and cache..')
os.remove('content.txt')
print('done!')