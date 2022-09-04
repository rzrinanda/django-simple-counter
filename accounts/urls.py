
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/<slug:', views.home, name='home-auth'),
    path('register', views.add, name='register'),
    path('login', views.login_request, name='login'),
    # path('logout/<int:id>', views.logout, name='logout'),
    path('logout', views.logout_request, name='logout'),
    path('ajax/counting', views.counting, name='counting')
    
]
