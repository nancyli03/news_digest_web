from django.shortcuts import render
from django.http import HttpResponse
import lxml.html
from .models import News
from django.utils import timezone
from django.shortcuts import render
from .utils import Utils
import re

# Create your views here.
def index(request):
    # Try to read from database for today's news
    print("Trying to read from database...")

    current_date = str(timezone.now().date())
    current_news = News.objects.filter(timestamp=current_date)

    if len(current_news) == 0:
        # Cannot find today's news, retrieve form website
        print("Cannot find today's news from database, read from website")
        url = "http://www.sina.com.cn"
        top_news_l = Utils.get_top_news(url)
        regex = '<a target="_blank" href="([^"]+)">([^<]+)</a>'
        for _news in top_news_l:
            found = re.match(regex, _news.strip())
            if not found:
                continue
            news_title = found.group(2)
            news_url = found.group(1)
            n = News(news_title=news_title, news_url=news_url, timestamp=current_date)
            n.save()
    else:
        print("Found from database")

    # Read from database
    print("Read from database")
    values = Utils.read_from_db()
    return  render(request, 'index.html', {'values': values})

def test(request):
    return HttpResponse("Hello World!")
