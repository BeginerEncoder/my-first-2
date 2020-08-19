from django.urls import path
from django.conf.urls.static import static
from first_2.settings import MEDIA_URL, MEDIA_ROOT
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.showcase, name = 'showcase'),
    path('<int:product_id>/', views.detail, name = 'detail'),
    path('<int:product_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('product_create/', views.leave_product, name = 'leave_product'),
] 