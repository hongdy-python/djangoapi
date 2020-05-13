from django.urls import path

from usersapp import views

urlpatterns = [
    path("user/", views.user),
    path("users/", views.UserView.as_view()),
    path("users/<str:pk>/", views.UserView.as_view()),

    path("students/", views.StudentView.as_view()),
    path("students/<str:pk>/", views.StudentView.as_view()),

    path("studentsapi/", views.StudentAPIView.as_view()),
    path("studentsapi/<str:id>/", views.StudentAPIView.as_view()),
]