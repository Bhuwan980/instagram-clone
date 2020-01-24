from django.urls import path
from . import views
urlpatterns = [
    path('',views.Authorlistview.as_view(),name='listview'),
    path('detail/<int:pk>',views.Authordetailview.as_view(),name='detail'),
    
]
