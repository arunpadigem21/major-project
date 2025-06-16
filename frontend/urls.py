

from django.urls import path
from . import views
from .views import active_ips

urlpatterns = [
    path('', views.signin, name='signin'),  # Default root goes to signin
    path('logout/', views.signout, name='logout'),

    path('home/', views.home, name='home'),  # Home page after login
    path('api/ip-stats/', views.ip_stats, name='ip_stats'),
    path('add-ip/', views.add_ip_view, name='add_ip'),
    path('deactivate-ip/', views.deactivate_ip, name='deactivate_ip'),
    path('toggle-ip-status/', views.toggle_ip_status, name='toggle_ip_status'),
    path('delete-ip/', views.delete_ip, name='delete_ip'),
    
    # API Endpoint
    path('api/active-ips/', active_ips, name='active_ips'),
   


]
