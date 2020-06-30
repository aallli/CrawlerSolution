##from tastypie.resources import ModelResource
#
#from rest_framework import resources
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

from tastypie.resources import ModelResource
from testapp.models import CRId2

class CRIdResource(ModelResource):
    class Meta:
        queryset = CRId2.objects.all()
        resource_name = 'resource'