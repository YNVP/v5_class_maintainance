from django import template
register = template.Library()
from django.template import loader
from attendance_request.models import AttendanceRequest
from datetime import datetime,timedelta


@register.simple_tag(takes_context=True)
def requests(context):
    request = context['request']
    requests=AttendanceRequest.objects.filter(user=request.user)
    return loader.get_template('attendance_request/tag_requests.html').render({
        'requests':requests,
    })