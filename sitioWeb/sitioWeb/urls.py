from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'sitioWeb.views.home', name='home'),
    url(r'', include('blog.urls')),
]
