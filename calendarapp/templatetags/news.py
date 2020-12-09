from django import template
register = template.Library()
from django.template import loader
from calendarapp.models import AddLatestNews
# import datetime
from datetime import datetime,timedelta

@register.simple_tag(takes_context=True)
def news(context):
    request = context['request']
    latest_news = AddLatestNews.objects.filter(end_time__gte=datetime.now(),created_time__gte=datetime.now()-timedelta(days=1))
    news=AddLatestNews.objects.filter(end_time__gte=datetime.now(),created_time__lt = datetime.now()-timedelta(days=1))
    return loader.get_template('calendarapp/latestnews.html').render({
        'news':news,
        'latest_news':latest_news,
    })