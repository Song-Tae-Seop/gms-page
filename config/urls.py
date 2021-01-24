"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('gms/', include('gms.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gms/', include('gms.urls')), #gms/로 접속이 들어오는 경우, gms.urls 파일에 있는 url 매핑을 참고하여 처리한다.
    path('', RedirectView.as_view(url='gms/', permanent=True)), #빈 경로로 접속이 들어오는 경우, /gms/로 처리한다.
]
