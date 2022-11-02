from django.urls import path
from . import views 

# app_name = "ifpi"

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path('page_login', views.page_login, name='page_login'),
    path('login_views', views.login_views, name='login_views'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('jogo_do_bicho', views.jogo_do_bicho, name='jogo_do_bicho'),
    path('loteria', views.loteria, name='loteria'),
    path('bet', views.bet, name='bet'),
    path("register", views.register_request, name="register"),
]
