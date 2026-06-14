from email.policy import default

from django.core.serializers import serialize
from django.shortcuts import render
from .models import Jobapplication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import JobApplicationSerializers
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication
# Create your views here.
class RegisterView(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self,request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff=True
        user.save()
        return Response({"message":"User created successfully"},
                        status=status.HTTP_201_CREATED)
# test1
# get all post
class JobListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        search=request.GET.get("search")
        status_filter=request.GET.get("status")
        jobs=Jobapplication.objects.filter(user=request.user)
        if search:
            jobs=jobs.filter(company_name__icontains=search)
        if status_filter:
            jobs=jobs.filter(status=status_filter)
        serializer=JobApplicationSerializers(jobs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=JobApplicationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class JobDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        job=get_object_or_404(Jobapplication,id=pk,user=request.user)
        serializer=JobApplicationSerializers(job)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        job = get_object_or_404(Jobapplication,id=pk,user=request.user)
        serializer=JobApplicationSerializers(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        job=get_object_or_404(Jobapplication,id=pk,user=request.user)
        job.delete()
        return Response({"message":"Job application has been deleted successfully"},status=status.HTTP_204_NO_CONTENT)

def register_page(request):
    return render(request,'register.html')
def login_page(request):
    return render(request,'login.html')
def dashboard_page(request):
    return render(request,'dashboard.html')
def add_job_page(request):
    return render(request, 'add-job.html')

