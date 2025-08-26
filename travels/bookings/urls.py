from .views import RegisterView,LoginView,BusListCreateView,UserBookingView,BookingView
from django.urls import path

urlpatterns = [
    path("buses/",BusListCreateView.as_view(),name='buslist'),
    path("register/",RegisterView.as_view(),name='register'),
    path("login/",LoginView.as_view(),name='login'),
    path("user/<int:user_id>/bookings/",UserBookingView.as_view(),name='user-bookings'),
    path("bookings/",BookingView.as_view(),name='bookings'),

]