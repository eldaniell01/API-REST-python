from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.book),
    path('list/', views.book_list),
    path('create/', views.book_create)
]
