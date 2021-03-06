from django.urls import path

from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.MyLoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/register/', views.register, name='register'),
    path('account/edit/', views.edit, name='edit'),
    path('account/writing/', views.write_post, name='writing'),
    path('account/author/<int:id>/', views.setpubtime, name='set_pubtime'),
    path('space/<int:id>/', views.visit_homepage, name='visit_homepage'),
]
