from django.urls import path
from .views import StudentGetAPI , StudentPostAPI, StudentPutAPI, StudentDeleteAPI

urlpatterns = [
    path('list/', StudentGetAPI.as_view(), name='list'),
    path('create/', StudentPostAPI.as_view(), name='create'),
    path('update/<pk>', StudentPutAPI.as_view(), name='put'),
    path('delete/<pk>', StudentDeleteAPI.as_view(), name='delete')
]