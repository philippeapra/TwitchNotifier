import requests
import discord
from books.twitch import send_twitch_request
from django.views.generic import ListView
from .models import Book
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from discord.ext import commands
from django.conf import settings
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

from django.views.decorators.csrf import csrf_exempt
import json
# Get the user's Discord ID (you can adjust this based on your app's user model)
user_id = "2579"  # Replace this with the user's Discord ID

# Create the message you want to send
message = "streamer online"

# Initialize the Discord bot client
bot_token = "MTEzMTE0NTY1MjY3MjM5NzMyMg.GvFYqu.tAcpfZMcmm_Rk6uR-KI2t0DuFRwwafIbxudb3k"
                    
@csrf_exempt
def eventsub_callback(request):
    if request.method == 'POST':
        print(request.POST)
        # Process the EventSub notification here
        # Access the payload using request.body or request.POST
        instance = Book.objects.first()
        payload= json.loads(request.body)
        if request.headers.get('Twitch-Eventsub-Message-Type')=="notification":
            if payload.get('subscription').get('type',"")=="stream.online":
                instance.title='streamer online'
                if request.method == 'POST':
                    

                    # https://discord.com/api/v9/channels/1132770961289125971/messages


                    discord_payload={
                            'content':message
                    }
                    header = {
                        'authorization':bot_token
                    }


                    r = requests.post("https://discord.com/api/v9/channels/1132770961289125971/messages", data=discord_payload,headers=header)
                    # intents = discord.Intents.default()
                    # intents.message_content = True
                    # bot = commands.Bot(command_prefix='!', intents=intents)

                    # # Find the user based on their ID
                    # user = await bot.fetch_user(int(user_id))

                    # if user:
                    #     # Send the message to the user
                    #     await user.send(message)
                    
                    
                    # bot = discord.Client()
                    # if user:
                    #         # Send the message to the user
                    #         await user.send(message)
                    #         #await bot.close()

                    # # Start the bot (it will execute the on_ready event)
                    # bot.run(bot_token)

                    #return render(request, '/books/book_list.html')


            elif payload.get('subscription').get('type',"")=="stream.offline":
                instance.title='streamer offline'
            else:
                instance.title='streamer in unknown state'
        instance.isbn = str(payload)
        if instance.title ==None:
            instance.title=""
        instance.save()
        if request.headers.get('Twitch-Eventsub-Message-Type')=='webhook_callback_verification':
            challenge = payload.get('challenge',"")
            return HttpResponse(status=200,content=challenge)
        return HttpResponseRedirect('/books/book_list.html',status=200)
    else:
        print(request.GET)
        return HttpResponse(status=405)

# Client_ID: 35a40a7mket0skoaja7p70i205qf8z
# Client_secret: 
