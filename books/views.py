from flask import  jsonify
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
    print ("zzzzzzzzzzzzzzrequest msg:")
    #print(request.GET)
    
    if request.method == 'POST':
        print(request.POST)
        # Process the EventSub notification here
        # Access the payload using request.body or request.POST
        # if challenge !=None:
        #     return jsonify({"challenge": challenge}), 200
            #send_twitch_request('eventsub/',{'challenge':challenge},None,"POST",None) 
        #instance.subtitle = request.POST.get('created_at')
        #instance.author = request.POST.get('status')
        instance = Book.objects.first()
        payload= json.loads(request.body)
        #instance.title=str(payload)
        challenge = payload['challenge']
        instance.isbn = str(payload)
        if instance.title ==None:
            instance.title=""
        instance.save()
        if request.headers.get('Twitch-Eventsub-Message-Type') == 'webhook_callback_verification':
            #return jsonify({"challenge": challenge}), 200
            return HttpResponse(status=200,content=challenge)
        return HttpResponseRedirect('/books/book_list.html',status=200)
    else:
        print(request.GET)
        return HttpResponse(status=405)



# Client_ID: 35a40a7mket0skoaja7p70i205qf8z
# Client_secret: d89jvmhf6ehs8lyt9qsbgx8exddc02
