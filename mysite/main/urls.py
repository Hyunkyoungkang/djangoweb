from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('notice_list/',views.list, name='notice_list'),
    path('notice/<int:id>',views.posting, name='post'),
    path('notice/add',views.notice_add, name='notice_add'),
    path('program/',views.program_view, name='program'),
]