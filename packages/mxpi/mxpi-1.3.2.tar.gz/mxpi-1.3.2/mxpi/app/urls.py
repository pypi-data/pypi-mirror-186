from django.urls import path
from . import views

app_name='app'

urlpatterns = [

path('',views.home,name='home'),
path('vnc',views.vnc,name='vnc'),
path('upfile_Ajax',views.upfile,name='upfile'),
path('file_list',views.file_list,name='file_list'),
path('file_remove',views.file_remove,name='file_remove'),
path('files',views.files,name='files'),
path('get_c',views.get_c,name='get_c'),
path('read_model_list',views.read_model_list,name='read_model_list'),
path('get_upmodel',views.get_upmodel,name='get_upmodel'),
path('getip',views.getip,name='getip'),
path('downModel',views.downModel,name='downModel'),
path('SArduino_get_list',views.SArduino_get_list,name='SArduino_get_list'),
path('SArduino_add_data',views.SArduino_add_data,name='SArduino_add_data'),
path('SArduino_get_data',views.SArduino_get_data,name='SArduino_get_data'),
path('mixly_ku_download',views.mixly_ku_download,name='mixly_ku_download'),
]
