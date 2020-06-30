from rest_framework import serializers
import pytz
from django.utils import timezone
#import jdatetime
#from django_jalali.db import serializers as jserializers


#status_timezone = pytz.timezone('Etc/GMT+2')
#now=timezone.now()
#class NameSerializer(serializers.Serializer):
#    keyword = serializers.ListField()
#    res_id = serializers.ListField()
#    created_at = serializers.DateTimeField(default=timezone.now())
#    
#from tastypie.resources import ModelResource

#from rest_framework import serializers
#from testapp.models import CR_TABLE
#
##from testapp.models import CR_TABLE
##class NoteSerializer(serializers.ModelSerializer):
##    class Meta:
##        model = Note
##        fields = '__all__'
#
#class CRTABLEResource(resources.ModelResource):
#    class Meta:
#        queryset = CR_TABLE.objects.all()
#        resource_name = 'crtable'
    
#from rest_framework import serializers 
from testapp.models import CRId2 

class CRId2Serializer(serializers.ModelSerializer):

    class Meta: 

        fields = (
            'request_id',
            'keyword',
            'res_ID',
            'created_at',
            'updated_at',    
        ) 

        model = CRId2