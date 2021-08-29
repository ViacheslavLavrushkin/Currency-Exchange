from accounts import views

from django.urls import path

app_name = 'account'

urlpatterns = [
    # path('my-profile/<int:pk>/', views.MyProfile.as_view(), name='my-profile'),
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('activate/account/<uuid:activation_key>/', views.ActivateAccount.as_view(), name='activate-account'),
]
