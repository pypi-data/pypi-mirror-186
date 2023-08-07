from django.urls import path

from . import views


app_name = "airavata_custos_portal_frontend"
urlpatterns = [
    path('', views.home, name="home"),
    path('tenants/default', views.home, name="home"),
    path('tenants/<str:clientId>/child-tenants', views.home, name="home"),
    path('tenants/<str:clientId>/child-tenants/new', views.home, name="home"),
    path('tenants/<str:clientId>', views.home, name="home"),
    path('tenants/<str:clientId>/profile', views.home, name="home"),
    path('tenants/<str:clientId>/users', views.home, name="home"),
    path('tenants/<str:clientId>/users/<str:username>', views.home, name="home"),
    path('tenants/<str:clientId>/groups', views.home, name="home"),
    path('tenants/<str:clientId>/groups/new', views.home, name="home"),
    path('tenants/<str:clientId>/groups/<str:groupId>', views.home, name="home"),
    path('tenants/<str:clientId>/permission-types/new', views.home, name="home"),
    path('tenants/<str:clientId>/permission-types', views.home, name="home"),
    path('tenants/<str:clientId>/roles/new', views.home, name="home"),
    path('tenants/<str:clientId>/roles', views.home, name="home"),
    path('tenants/<str:clientId>/entity-types/new', views.home, name="home"),
    path('tenants/<str:clientId>/entity-types', views.home, name="home"),
    path('tenants/<str:clientId>/entities/new', views.home, name="home"),
    path('tenants/<str:clientId>/entities', views.home, name="home"),
    path('tenants/<str:clientId>/entities/<str:entityId>', views.home, name="home"),
]
