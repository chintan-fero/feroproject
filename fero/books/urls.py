from django.urls import path

from . import views

urlpatterns = [
    path('book_list', views.book_list, name='book_list'),
    path('book_detail/<int:question_id>/', views.book_detail, name='book_detail'),
]
