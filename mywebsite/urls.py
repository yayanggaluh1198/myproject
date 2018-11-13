from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^about/', include('about.urls')),
	url(r'^blog/', include('blog.urls')),
	url(r'^pendaftaran/', include('pendaftaran.urls',namespace='pendaftaran')),
	url(r'^$', views.index),
]
