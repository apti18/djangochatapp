from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Home page should be at the root
    path('login/', views.LoginForm, name="login"),
    path('logout/', views.LogoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('room/<str:pk>/', views.room, name="room"),  # Room detail view
    path('profile/<str:pk>/', views.userProfile, name="userprofile"),  # User profile view
    path('createroom/', views.createRoom, name="createroom"),
    path('updateroom/<str:pk>/', views.updateRoom, name="updateroom"),
    path('deleteroom/<str:pk>/', views.deleteRoom, name="deleteroom"),
    path('deletemessage/<str:pk>/', views.deleteMessage, name="deletemessage"),
    path('updateuser/', views.updateUser, name="updateuser"),
    path('topics/', views.browseTopic, name="topics"),
    # path('activityp/', views.activityPage, name="activityp"),
]
