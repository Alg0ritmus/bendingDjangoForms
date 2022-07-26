from django import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name="base"
urlpatterns = [
    path('', views.home, name="home"),
    path('users/', views.getPersons, name="getPersons"),
    path('testFormsets/', views.testFormsets, name="testFormsets"),
    path('postModelInfo/', views.postModelInfo, name="postModelInfo"),
    path('updateModelInfo/<int:pk>', views.updateModelInfo, name="updateModelInfo"),
    path('modelFormSets/',views.modelFormSets,name="modelFormSets"),
    path('DoubleOneToMany/',views.DoubleOneToMany,name="DoubleOneToMany"),
    path('NBAforms/',views.NBAforms,name='NBAforms'),
    path('FetchReq/',views.FetchReq,name='FetchReq'),
    path('uploadFile/', views.uploadFile, name='uploadFile'),
    path('uploadMultipleFiles/', views.uploadMultipleFiles, name='uploadMultipleFiles'),
    path('deleteAllFiles/', views.deleteAllFiles, name='deleteAllFiles'),
    re_path(r'^restrictedFiles/(?P<mypath>.*)$',views.restrictedFiles, name= 'restrictedFiles'), 
    
]

# re_path to resolve path: https://docs.djangoproject.com/en/4.0/ref/views/#django.views.static.serve


# make path for get req
# https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-uploaded-files-in-development

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)