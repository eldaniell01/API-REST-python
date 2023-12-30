from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.Books.as_view()),
    path('list/', views.BookList.as_view()),
    path('create/', views.BookCreate.as_view())
]
