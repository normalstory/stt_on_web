from django.conf.urls import url 
from . import views 

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^a$', views.page_a, name='page_a'),
    url(r'^b$', views.page_b, name='page_b'),
    url(r'^c$', views.page_c, name='page_c'), 
]
