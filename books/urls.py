from django.urls import path
from .views import BookListView
from .views import eventsub_callback
urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path('eventsub/subscriptions', eventsub_callback, name='eventsub_callback'),
]