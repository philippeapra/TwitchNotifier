from django.views.generic import ListView
from .models import Book
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"



# Client_ID: 35a40a7mket0skoaja7p70i205qf8z
# Client_secret: d89jvmhf6ehs8lyt9qsbgx8exddc02
