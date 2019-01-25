"""Define all util functions"""
import lxml.html
import urllib.request
from .models import News


class Utils():
    @classmethod
    def get_top_news(self, url):
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        html = mybytes.decode("utf8")
        fp.close()
        root = lxml.html.document_fromstring(html)
        top_news = root.xpath('//ul[contains(@class, "list-a news_top")]')[0]
        tmp_top_news = lxml.html.tostring(top_news).decode("utf-8")
        tmp_top_news = tmp_top_news.replace("</li>", "<li>")
        return tmp_top_news.split("<li>")

    @classmethod
    def read_from_db(self):
        entries = News.objects.all()
        dates = []
        values = []
        # Construct a dict like this:
        """
        [
            {"date":date, "values": news_entries}
        ]
        """
        for entry in entries:
            if len(dates) == 0:
                dates.append(entry.timestamp)
            elif entry.timestamp not in dates:
                dates.append(entry.timestamp)

        for i in range(len(dates)):
            date = dates[i]
            news_entries = News.objects.filter(timestamp=date)
            tmp_dict = {
                'date': date,
                'values': news_entries
            }
            values.append(tmp_dict)

        return values
