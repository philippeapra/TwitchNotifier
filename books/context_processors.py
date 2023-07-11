from books.twitch import subscribe_user
import requests
from books.models import Book

def is_stream_live(request):
    
    instance = Book.objects.first()

    subscribe_user(7)
    
    #context = {'zzz': "zzz"}
    #book = request.user.username
    #context = {'zzz': 'zzz'}
    return {'status': instance}
    #return HttpResponseRedirect("/")
    #context = {'username': "phil"}
    #return render(request, 'books/book_list.html', context)