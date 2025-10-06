from django.urls import path 
from blog import views # type: ignore

urlpatterns=[
    path('',views.home,name='home'),
    path('blog/<int:id>/',views.blog_detail,name='blog_detail'),
]