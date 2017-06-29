from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^teacher/', include('teacher.urls')),
	url(r'^$', include('teacher.urls')),
]