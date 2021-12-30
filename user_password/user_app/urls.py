from django.conf.urls import url
from user_app import views

#TEMPLATE TAGGING [TEMPLATE URLS!]
app_name ='user_app'

urlpatterns=[
    url('register/',views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
]

