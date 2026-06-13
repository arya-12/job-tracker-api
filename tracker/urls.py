from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from  .views import JobDetails,JobListView,RegisterView,login_page,register_page,dashboard_page,add_job_page


urlpatterns=[
path('api/register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('jobs/',JobListView.as_view()),
    path('jobs/<int:pk>/',JobDetails.as_view()),

    path('', login_page),
    path('register/', register_page),
    path('dashboard/', dashboard_page),
    path('add-job/', add_job_page),
]
