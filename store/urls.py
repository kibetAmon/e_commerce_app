from django.urls import path
from . import views
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('store/', views.store, name='store'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),  # This should be defined
    path('logout/', views.logout, name='logout'),
    path('cart/', auth_middleware(views.Cart.as_view()), name='cart'),
    path('check-out/', views.CheckOut.as_view(), name='checkout'),
    path('orders/', auth_middleware(views.OrderView.as_view()), name='orders')
]
