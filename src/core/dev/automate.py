import os
from django import forms
# from resource.models import (
#     Book,
#     Resource,
#     Author
# )

def create_author(name):
    pass

def create_book(user, isbn, title, author, image):
    pass

def load_books(csv_dirs, csv_file, size):
    pass

def automate(books, user, image_dirs):
    pass

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
    
    if os.path.exists(path):
        path_exist = True
    
    return path_exist, path

CSV_DIRS = ['data', 'cleaned']
CSV_FILE = 'clean_books_6939.csv'
IMAGE_DIRS = ['cleaned_image_all']

print(get_path(CSV_DIRS,CSV_FILE))
