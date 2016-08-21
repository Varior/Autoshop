"""avtodec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based view
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from batteries.views import AboutUs, Contacts
from main.views import Main



urlpatterns =[ 
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main.as_view(), name='main' ),
    url(r'^batteries/$', 'batteries.views.index', name='batteries' ),
    url(r'^about/$', AboutUs.as_view(), name ='about'),
    url(r'^contacts/$', Contacts.as_view(), name ='contact'),
    url(r'^battery/(?P<slug>[^/]+)/$', 'batteries.views.car_battery_detail', name = 'battery'),
 ] +  static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
 ) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
 )
 