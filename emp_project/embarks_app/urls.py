from . import views
from django.urls import path

urlpatterns = [
    path('',views.Mten,name='jazz'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]
