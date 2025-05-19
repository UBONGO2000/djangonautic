from . import views
from django.urls import path


urlpatterns = [
    path('', views.articles_list,name='list'),
    path('<slug:slug>/',views.articles_detail,name='detail')
    
]
