from books.twitch import send_twitch_request
from django.views.generic import ListView
from .models import Book
from django.http import HttpResponse
from django.http import HttpResponseRedirect
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def eventsub_callback(request):
    if request.method == 'POST':
        print(request.POST)
        # Process the EventSub notification here
        # Access the payload using request.body or request.POST
        instance = Book.objects.first()
        if request.headers.get('Twitch-Eventsub-Message-Type') == 'notification':
            instance.title='streamer online'
        payload= json.loads(request.body)
        try:
            challenge = payload['challenge']
        except:
            challenge=None
        instance.isbn = str(payload)
        if instance.title ==None:
            instance.title=""
        instance.save()
        if request.headers.get('Twitch-Eventsub-Message-Type') == 'webhook_callback_verification':
            return HttpResponse(status=200,content=challenge)
        return HttpResponseRedirect('/books/book_list.html',status=200)
    else:
        print(request.GET)
        return HttpResponse(status=405)

# Client_ID: 35a40a7mket0skoaja7p70i205qf8z
# Client_secret: 
