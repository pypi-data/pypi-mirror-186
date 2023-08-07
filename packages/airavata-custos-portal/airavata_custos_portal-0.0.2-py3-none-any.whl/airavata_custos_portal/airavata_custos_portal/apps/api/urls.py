from django.urls import path

from . import views

urlpatterns = [
    path("config", views.get_config),
    path("userinfo", views.get_userinfo),
    path('callback', views.get_auth_callback),
    path('custos/<path:endpoint_path>', views.get_custos_api)
]
