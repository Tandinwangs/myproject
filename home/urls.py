from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.userLogin, name="user-login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.userRegister, name="user-register"),
    path('success/', views.success, name="success"),
    
    path('profile/', views.userProfile, name="profile"),
    path('queue/', views.video, name="queue"),
    path('session/', views.userSession, name="session"),
    # path('generate-queue/', views.generateQueue, name="generate-queue"),
    path('user-update/', views.userUpdate, name="user-update"),

    # path('user-delete/<queue_id>', views.deleteQueue, name="delete-queue"),
    path('reserve-gym/', views.reserveSession, name="reserve-gym"),
    path('user-session/<session_id>', views.deleteSession, name="delete-session"),
]
