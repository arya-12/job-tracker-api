from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from  .views import JobDetails,JobListView,RegisterView


urlpatterns=[
path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('jobs/',JobListView.as_view()),
    path('jobs/<int:pk>/',JobDetails.as_view())
]
