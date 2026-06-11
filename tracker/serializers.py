from django.contrib.admin.utils import model_ngettext
from rest_framework import serializers
from .models import Jobapplication

class JobApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Jobapplication
        fields=['id','company_name','job_title','status','notes','date_applied']
        read_only_fields=['date_applied']

