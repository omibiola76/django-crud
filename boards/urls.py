from boards.views import ( Home, AddNewCli, Tables, WhiteBoard )
from django.conf.urls import url
from django.urls import path

urlpatterns =  [
    path('home/', Home.as_view(), name='boards-home'),
    path('addnewcli/', AddNewCli.as_view(), name='boards-addnewcli'),
    path('tables/', Tables.as_view(), name='boards-tables'),
    path('whiteboard/', WhiteBoard.as_view(), name='boards-whiteboard'),
]
