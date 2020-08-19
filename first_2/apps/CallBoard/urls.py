from django.urls import path

from . import views

app_name = 'advert'
urlpatterns = [
    path('', views.board, name = 'board'),
    path('advert_create/', views.leave_advert, name = 'leave_advert'),
    path('<int:advert_id>/', views.detail, name = 'detail'),
    path('<int:advert_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]