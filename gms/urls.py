from django.urls import path
from gms import views
from django.views.generic import RedirectView

app_name='gms'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]   #url이 일치하면 views.py에서 해당하는 함수를 불러온다.