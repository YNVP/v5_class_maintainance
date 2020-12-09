from calendarapp.models import *
from datetime import datetime,timedelta
def remove_objects():
    old_news = AddLatestNews.objects.filter(end_time__lt = datetime.now())
    old_events = Event.objects.filter(end_time__lt = datetime.now()-timedelta(days=62))
    old_news.delete()
    old_events.delete()
remove_objects()