import pandas as pd
import numpy as np
import csv

from urllib.request import urlretrieve
from urllib.parse import urlsplit
import os

from PIL import Image

import time
start_time = time.time()

def load_data(filename,sep=',', limit=None):
    SIZE = 10
    # book_df = pd.read_csv(filename,  sep=';',engine='python', quotechar='"', error_bad_lines=False).iloc[1:SIZE, 1:]
    book_df = pd.read_csv(filename,  sep=sep,engine='python', quotechar='"', error_bad_lines=False).iloc[1:SIZE, 1:]
    
    book_list = book_df.values.tolist()
    books = [] #{'isbn': , 'authors': [], 'year_of_pub': , 'publisher': , 'img_urls': [] }
    '''
    for i in range(len(book_list)):
        isbn = book_list[i][0]
        title = book_list[i][1]
        authors = book_list[i][2:-5]
        year_of_pub = book_list[i][-5]
        publisher = book_list[i][-4]
        img_urls = book_list[i][-3:]

        books.append({'isbn': isbn , 'title':title, 'authors': authors, 'year_of_pub':year_of_pub ,'publisher': publisher , 'img_urls': img_urls })

    print('books:', book)
    '''
    return book_list

def load_csv(size=10, all=False):
    SIZE = size
    CSV_FILE_PATH = 'data\\BX-Books.csv'
    with open(CSV_FILE_PATH) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(14734))

    if all:
        bookdf = pd.read_csv(CSV_FILE_PATH, engine='python', dialect=dialect, error_bad_lines=False) #.iloc[:, :]
    else:
        bookdf = pd.read_csv(CSV_FILE_PATH, engine='python', dialect=dialect, error_bad_lines=False).iloc[:SIZE, :]

    book_list = bookdf.values.tolist()
    books = []
    multiple_author = 0
    for i in range(len(book_list)):
        isbn = book_list[i][0]
        title = book_list[i][1]
        author = book_list[i][2]
        year_of_pub = book_list[i][3]
        publisher = book_list[i][4]
        img_urls = book_list[i][-3:]
        url = book_list[i][-1]
        # if len(authors)>1:
        #     multiple_author += 1
        #     print(f'len= {len(authors)} and authors= {authors}')
        if type(year_of_pub) != int:
            print(year_of_pub)
        books.append({'isbn': isbn , 'title':title, 'author': author, 'year_of_pub':year_of_pub ,'publisher': publisher , 'img_urls': img_urls, 'url': url })
    # print(f'Found multiple_author = {multiple_author}')
    return books

def check_img(filename,min_w=10, min_h=10, remove=False):
    # try:  
    #     img  = Image.open(path)  
    # except IOError: 
    #     pass
    ok = False
    with Image.open(filename) as image: 
        width, height = image.size
        if width >= min_w or height >= min_h:
            ok = True
        # print('width:',width, 'height:',height, 'Status:',ok)
    
    if not ok:
        if remove and os.path.isfile(filename):
            ## If file exists, delete it ##
            os.remove(filename)
    return ok

def img_download(url, filename, filedir=None):
    status = False
    if filedir:
        if os.path.isdir(filedir):
            pass
        else:
            os.mkdir(filedir)
        filename = os.path.join(filedir, filename)
        # dirpath = ''
        # for dir in filedir:
        #     dirpath = os.path.join(dirpath, dir)
        # if os.path.exists(dirpath):
        #     filename = os.path.join(dirpath, filename)
        # else:
        #     os.mkdir(dirpath)
        #     filename = os.path.join(dirpath, filename)
    try:
        img, header = urlretrieve(url, filename) # returns (filename, headers)
        status = check_img(img, remove=True)
        # print('filename=', filename)
        # print('url=',url)
        # print('img=',img)
        # print('header=',header)
    except:
        print("ERROR in download img! url=",url)
    
    return status

def img_offline_check(filename, filedir=None):
    status = False
    if filedir:
        if os.path.isdir(filedir):
            filename = os.path.join(filedir, filename)
    if os.path.exists(filename):
        status = True
    
    return status

def to_url_list(url_str):
    url_str_list = url_str.lstrip('[] ').split(',')
    urls = [urlsplit(url) for url in url_str_list]
    print(urls)
    print([url.geturl for url in urls])

    # from urllib.parse import urlsplit
    # url = 'HTTP://www.Python.org/doc/#'
    # r1 = urlsplit(url)
    # r1.geturl()
    # 'http://www.Python.org/doc/'
    # r2 = urlsplit(r1.geturl())
    # r2.geturl()
    # 'http://www.Python.org/doc/'
    return urls

def get_cleaned_data(books, filedir, download=False):
    clean_books = []
    succeed = 0
    failed = 0
    for i, book in zip(range(len(books)), books):
        # {'isbn': isbn , 'title':title, 'author': author, 'year_of_pub':year_of_pub ,'publisher': publisher , 'img_urls': img_urls, 'url': url }
        filename = book['isbn'] + '.jpg'
        url = book['url']

        if download:
            result = img_download(url, filename, filedir)
        else:
            result = img_offline_check(filename, filedir)
        # result = True
        if result: 
            succeed += 1
            isbn = book['isbn']
            title = book['title']
            author = book['author']
            year_of_pub = book['year_of_pub']
            publisher = book['publisher']
            url = book['url']
            image = filename
            clean_books.append({'isbn': isbn, 'title': title, 'author': author, 'year_of_pub':year_of_pub ,'publisher': publisher , 'url': url, 'image': image})
        else:
            failed += 1

        # print('Result:', result)

    print(f'Total={succeed+failed}, succeed={succeed}, failed={failed}')

    return clean_books


books = load_csv(size=10, all=True)
clean_books = get_cleaned_data(books, filedir='test')
print('book=', books[0]) 
print('clean Book=', clean_books[0])

if False:
    FILE_NAME = 'data\\cleaned\\clean_books.csv'
    clean_df = pd.DataFrame(clean_books, columns=['isbn','title','author','year_of_pub','publisher','url', 'image'])
    clean_df.to_csv(FILE_NAME, index=False) #, index_label="ID", sep=','


print(f'book_len={len(books)} and cleaned_book_len={len(clean_books)}')

print('Time needed=', (time.time() - start_time)/60)