import os
import requests
import codecs


#tao thu muc
def make_dir(name):
    os.mkdir(name)
    os.chdir(name)

#luu file
def save(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()

#luu tat ca file
def save_all(history, page_max):
    for (stt, url_new_sub) in enumerate(history):
        if stt >= page_max:
            break
        save_file(url_new_sub, stt)
        print(f'{stt} {url_new_sub}')
