from django.views.generic import ListView
from .models import Book
from django.http import HttpResponse
from django.http import HttpResponseRedirect
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def eventsub_callback(request):
    #print ("zzzzzzzzzzzzzzrequest msg:")
    #print(request.GET)
    
    if request.method == 'POST':
        print(request.POST)
        # Process the EventSub notification here
        # Access the payload using request.body or request.POST
        # Perform necessary actions based on the event data received
        # ...
        print ("zzzzzzzzzzzzzzrequest msg:")
        #print (request.POST.jsonify)
        instance = Book.objects.first()
        instance.title = "subscribed"
        instance.save()
        return HttpResponseRedirect('/books/book_list.html',status=200)
    else:
        print(request.GET)
        return HttpResponse(status=405)



# Client_ID: 35a40a7mket0skoaja7p70i205qf8z
# Client_secret: d89jvmhf6ehs8lyt9qsbgx8exddc02
