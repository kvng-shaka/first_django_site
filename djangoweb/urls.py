"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, contact, gallery, reservation
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import form_view, blog, blog_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('reservation/', reservation, name='reservation'),
    path('newpost/', form_view, name='newpost'),
    path('blog/', blog, name='blog'),
    path('blog_details/<int:pk>', blog_details, name='blog-details'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
