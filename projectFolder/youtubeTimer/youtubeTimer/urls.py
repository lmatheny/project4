from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    
    path('CNIT581-048-Milestone4/', include('finalapp.urls')),
    path('admin/', admin.site.urls),
    path('person/', include('finalapp.urls')),
    path('home/', include('finalapp.urls')),
    path('stopwatch/', include('finalapp.urls')),
    path('newDay/', include('finalapp.urls')),
    path('success_page/', include('finalapp.urls')),
    path('calendar/', include('finalapp.urls')),
    path('CNIT581-048-Milestone4/', include('finalapp.urls')),
]