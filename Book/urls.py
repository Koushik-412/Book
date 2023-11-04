
from django.urls import path
from .views import *

urlpatterns = [
    # path("",home),
    path("",Booklist),
    path("add/",postBooklist),
    path("update/<int:id>/",updateBooklist),
    path("delete/<int:id>/",deleteBooklist),
]