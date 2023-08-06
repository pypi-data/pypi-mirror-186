from django.urls import path
from . import views
urlpatterns = [
    path('set_google', views.set_google, name="set_google"),
    path('auth_return', views.auth_return, name="auth_return"),
    path('select_property', views.select_property, name="select_property"),
    path('set_property/<int:track_id>', views.set_property, name="set_property"),
]
