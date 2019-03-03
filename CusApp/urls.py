from django.urls import path, re_path
from CusApp import views


app_name = "CusApp"

urlpatterns = [
    path("AddCustomer/", views.AddCustomer.as_view(), name = "AddCustomer"),
    path("Logout/", views.Logout_View.as_view(), name = "Logout"),
    path("Customer/", views.index.as_view(), name = "Customer"),
    path('', views.index.as_view(), name="index"),
    path("Search/", views.Search_View.as_view(), name = "Search"),
    path("login/", views.Login_View.as_view(), name = "login"),
    path("signup/", views.Sigup_View.as_view(), name= "signup"),
    path(r'^(?P<pk>\d+)/itemdelete/$', views.DeleteItem.as_view(), name = 'DeleteItem' ),
    path(r'^(?P<pk>\d+)/Profile/$', views.Customer_View.as_view(), name = 'CustomerView' ),
    path("submitted/", views.Submitted_View.as_view(), name = "submitted"),
    re_path('cart/', views.Cart_View.as_view(), name = 'cart' ),




]
