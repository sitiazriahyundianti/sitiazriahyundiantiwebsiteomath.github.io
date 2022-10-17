"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from beranda.views import beranda
from kontak.views import kontak
from materi.views import materi
from materi2.views import materi2
from materi3.views import materi3
from materi4.views import materi4
from rangkuman.views import rangkuman
from soal.views import soal


urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda/', beranda),
    path('kontak/', kontak),
    path('materi/', materi),
    path('materi2/', materi2),
    path('materi3/', materi3),
    path('materi4/', materi4),
    path('rangkuman/', rangkuman),
    path('soal/', soal),


]
