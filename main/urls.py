from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('user.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('nadmin/',admin.site.urls),
    path('comment/', include('comment.urls')),
    path("account/", include("account.urls")),
    path('tinymce/', include('tinymce.urls')),
    path("blog/", include("blog.urls")),
    path("teams/", include("teams.urls")),
    path("meeting/", include("meeting.urls")),
    path("attendance_request/", include("attendance_request.urls")),
    path("contact/", include("contacts.urls")),
    path("event/", include("calendarapp.urls")),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('todo/', include('todo.urls', namespace="todo")),
    # path('robots.txt',robots),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
