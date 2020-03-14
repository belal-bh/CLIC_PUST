import os
import pandas as pd
import numpy as np
import csv

# from django.shortcuts import render
# from django.contrib import messages
# from django.contrib.contenttypes.models import ContentType
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# import datetime
# from django.contrib.auth.decorators import login_required




from resource.models import (
    Book,
    Resource,
    Author
)

# from .forms import (
#     BookForm,
#     AuthorForm,
# )

def create_author(name):
    # form = AuthorForm(None, None)
    nicname = name.split(' ')[0]
    if len(name)> 99:
        print(f'WOW!!! Author name({len(name)}:{name})')
        name = name[:99]
    if len(nicname) > 30:
        print(f'WOW!!! Author nicname({len(nicname)}:{nicname}) [ Author= {name}]')
        nicname = nicname[:30]

    obj, created = Author.objects.get_or_create(name=name, nicname=nicname)
    if created:
        print(f'author created={obj.name}')
        return obj, created
    elif obj:
        print(f'author got={obj.name}')
        return obj, created
    else:
        print('ERROR in author creation!')
        print('name=',name,' and nicname=',nicname)
        return None, False
    

def create_book(user, isbn, title, author, publisher, image):
    # title = 
    # author = 
    accession_number = isbn
    call_number = isbn
    copy_number = isbn
    # isbn = 
    # publisher =
    language = 'English'
    image_path = image
    # user = 
    work_done = 10
    obj, created = Book.objects.get_or_create(title=title, accession_number=accession_number,call_number=call_number,copy_number=copy_number,isbn=isbn, publisher=publisher,language=language,added_by=user,work_done=work_done)
    # obj, created = Book.objects.get_or_create(title=title, author=author, accession_number=accession_number,call_number=call_number,copy_number=copy_number,isbn=isbn, publisher=publisher,language=language,added_by=user,work_done=work_done)
    # obj, created = Book.objects.get_or_create(title=title, author=author, accession_number=accession_number,call_number=call_number,copy_number=copy_number,isbn=isbn, publisher=publisher,language=language,image=image_path,added_by=user,work_done=work_done)
    if created:
        obj.image = image_path
        obj.author.add(author)
        obj.save()
        print(f'Book Created = {obj.title} image={obj.image.url}')
        return obj, created
    elif obj:
        obj.image = image_path
        if author not in obj.author.all():
            obj.author.add(author)
        obj.save()
        print(f'Book got = {obj.title} and image={obj.image.url}')
        return obj, created
    else:
        print(f'ERROR book creation! isbn={isbn}')
        return None, False

def get_path(dirs=[], filename=None, abs_path=False):
    if abs_path:
        path = os.path.abspath('')
    else:
        path = ''
    path_exist = False
    for filedir in dirs:
        path = os.path.join(path, filedir)
    if filename:
        path = os.path.join(path, filename)
    
    print('path=',path)

    if os.path.exists(path):
        path_exist = True
    
    return path_exist, path


def load_books(csv_dirs, csv_file, size=None, all=False):
    if size:
        SIZE = size
    else:
        all = True

    status, CSV_FILE_PATH = get_path(dirs=csv_dirs, filename=csv_file)
    if status:
        print('CSV_FILE_PATH=',CSV_FILE_PATH)
    else:
        return []

    if all:
        bookdf = pd.read_csv(CSV_FILE_PATH, engine='python', error_bad_lines=False) #.iloc[:, :] #, dialect=dialect
    else:
        bookdf = pd.read_csv(CSV_FILE_PATH, engine='python', error_bad_lines=False).iloc[:SIZE, :] #dialect=dialect, 

    books = bookdf.values.tolist()
    return books

def automate(books, user, image_dirs):
    new_author_created = 0
    new_book_created = 0
    succeed = 0
    failed = 0
    total_book = len(books)
    for book in books:
        # {'isbn': 0, 'title': 1, 'author': 2, 'year_of_pub':3 ,'publisher': 4 , 'url': 5, 'image': 6}
        author_name = book[2]
        author_obj, author_created = create_author(author_name)
        # print(f'user={user}, image_dir={get_path(dirs=image_dirs,filename=book[-1])}')

        if author_created:
            new_author_created += 1

        if author_obj:
            book_isbn = book[0]
            book_title = book[1]
            book_author = author_obj
            book_publisher = book[4]

            # ########################
            # Note: manualy have to copy all required file before book creation in media_cdn/automated/ directory
            # book_image = book[6]
            img_exsists, img_path = get_path(dirs=['automated'],filename=book[-1])
            # img_exsists, img_path = get_path(dirs=image_dirs,filename=book[-1])
            if img_exsists:
                book_image = img_path
            else:
                book_image = img_path
            # ########################
            book_obj, book_created = create_book(user=user, isbn=book_isbn, title=book_title, author=book_author, publisher=book_publisher, image=book_image) 
            if book_created:
                new_book_created += 1
                print(f'Book created= {book_obj.title}, Author= {book_obj.author} , Image_url={book_obj.image.url}')
            elif book_obj:
                succeed += 1
                print(f'Book  got= {book_obj.title}, Author= {book_obj.author}, Image_url={book_obj.image.url}')
            else:
                failed += 1
                print(f'FAILED!! isbn={book_isbn}')
    status = {
        'new_author_created': new_author_created,
        'new_book_created': new_book_created,
        'succeed': succeed,
        'failed': failed,
        'total_book': total_book,
    }

    return status
        
