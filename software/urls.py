from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.developer_Dashboard),


    #***************************** Manager ******************************
    
    path('manager_Dashboard',views.manager_Dashboard),
]
