from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.BookCreateView.as_view(),name="create"),
    path('book_detail/<int:pk>',views.BookDetailView.as_view(),name="book_detail"),
    path('mysite/',views.mysite,name="mysite"),
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('book_loan/',views.BookInstanceView.as_view(),name="book_loan"),
]
