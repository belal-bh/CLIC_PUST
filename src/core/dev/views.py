from django.shortcuts import render
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required


from account.models import User
from resource.models import (
    Book,
    Resource,
)

from wishlist.models import (
    BookCart,
    ResourceCart,
)

from transaction.models import (
    TrxBook,
    TrxResource,
)



from .automate import *
from .forms import (
    BookForm,
    AuthorForm,
)

#D:\Challenges\pust\dev\CLIC_PUST\src\core\dev\data\cleaned\clean_books_6939.csv
CSV_DIRS = ['data', 'cleaned']
CSV_FILE = 'clean_books_6939.csv'
IMAGE_DIRS = ['data', 'cleaned','cleaned_image_all']

@login_required
def dev_view(request):
    user_instance = request.user
    if not request.user.is_superuser:
        return redirect('/')
    
    form = BookForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        print(request.POST)
        if 'automate' in request.POST.keys():
            # FILE_NAME = 'core\\dev\\data\\abc.csv'
            # print(os.getcwd())
            # form = BookForm(request.POST or None, request.FILES or None)
            # books = load_books(csv_dirs=CSV_DIRS,csv_file=FILE_NAME,size=10)
            books = load_books(csv_dirs=CSV_DIRS,csv_file=CSV_FILE)
            #['195153448', 'Classical Mythology', 'Mark P. O. Morford', 2002, 'Oxford University Press', 'http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', '0195153448.jpg']
            # print('books=', books[0])
            status = automate(books,user_instance,IMAGE_DIRS)
            print(f'status = {status}')

            

    # print(get_path(CSV_DIRS,CSV_FILE))

    context = {
        'title': "Dev Admin Section",
        'instance': request.user,
        'form': form,
    }
    return render(request, 'automate_admin.html', context)