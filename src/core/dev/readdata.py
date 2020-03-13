import pandas as pd
import numpy as np
import math


# import python-slugify to convert product_name as slug_string
# pip install python-slugify
# from slugify import slugify

################### LOAD DATA ###########################
def load_data():
    print("Loading Data...")
    F_1 = 'data\\BX-Book-Ratings.csv'
    F_2 = 'data\\BX-Books.csv'
    F_3 = 'data\\BX-Users.csv'

   
    ZIZE = 100
    # df1 = pd.read_csv(F_1).iloc[1:ZIZE, [1,16]] 
    # df2 = pd.read_csv(F_2).iloc[1:ZIZE, [3,20]] 
    # df3 = pd.read_csv(F_3).iloc[1:ZIZE, [3,20]]

    # "ISBN";"Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"
    
    book_df = pd.read_csv(F_2,  sep=';',engine='python', quotechar='"', error_bad_lines=False) #.iloc[1:ZIZE, [1,2]] 
    # book_df = pd.read_csv(F_2,  header=None, error_bad_lines=False,  encoding='utf-8').iloc[1:ZIZE, [1,2]] 

    print("Data Loaded")
    return book_df

def load_csv():
    # import requests
    import csv
    with open('data\\BX-Books.csv') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(14734))


    df = pd.read_csv('data\\BX-Books.csv', engine='python', dialect=dialect, error_bad_lines=False)
    return df

bookdf =  load_csv() #load_data()
book_list = bookdf.values.tolist()
# isbn = []
# authors = []
# year_of_pub = []
# publisher = [],
# img_url = []

book = [] #{'isbn': , 'authors': [], 'year_of_pub': , 'publisher': , 'img_urls': [] }

for i in range(len(book_list)):
    isbn = book_list[i][0]
    authors = book_list[i][1:-5]
    year_of_pub = book_list[i][-5]
    publisher = book_list[i][-4]
    img_urls = book_list[i][-3:]

    book.append({'isbn': isbn , 'authors': authors, 'year_of_pub':year_of_pub ,'publisher': publisher , 'img_urls': img_urls })

print('books:', book)

book_df = pd.DataFrame(book, columns=["isbn","authors","year_of_pub","publisher","img_urls"])
book_df.to_csv('data\\output\\books.csv')
# FILE_NAME = 'data\\output\\book_sniff.csv'

# df = pd.DataFrame(bookdf, columns=["ISBN","Book-Title","Book-Author","Year-Of-Publication","Publisher","Image-URL-S","Image-URL-M","Image-URL-L"])
# df.to_csv(FILE_NAME, index=True, index_label="ID", sep=';')
# bookdf.to_csv()
