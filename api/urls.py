from django.urls import path
from . import views 


app_name = 'api'

urlpatterns = [
    
    path('',views.book_list,name='book_list'),
    path('book_detail/<id>/',views.book_detail,name='book_detail'),
    path('add_book/',views.add_book,name='add_book'),
    path('update_book/<id>/',views.update_book,name='update_book'),
    path('delete_book/<id>/',views.delete_book,name='delete_book')
]
