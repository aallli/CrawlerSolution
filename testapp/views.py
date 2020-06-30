from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import CRId2Serializer
import pika
import json
from testapp.models import CRId2 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.143.17',port=5672,credentials=credentials))

class SegmentcliApiList(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
#        resource = ['tlgrm', 'instgrm', 'twtr']
#        res_id=[1,2,3]
        return Response(status=404)
    
    
    queryset = CRId2.objects.all() 
    serializer_class = CRId2Serializer
    def post(self, request, *args, **kwargs):
        serializer = CRId2Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
#        if serializer.is_valid():
#        .objects.create
        self.perform_create(serializer)
#        CR_TABLE.objects.create(keyword=keyword,res_ID=chan)
        headers = self.get_success_headers(serializer.data)
        
#            keyword = serializer.data.get('keyword')
#            res_id = serializer.data.get('res_id')
        return Response(
                {'id': serializer.data.get('request_id')},
                status=status.HTTP_201_CREATED,
                headers=headers
                )


    
        


    def put(self, request, *args, **kwargs):
        return Response({'response': 'This response from put method'})

    def patch(self, request, *args, **kwargs):
        return Response({'response': 'This response from patch method'})

    def delete(self, request, *args, **kwargs):
#        serializer = CRId2Serializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        id= CRId2Serializer.data.get('request_id')
#        CRId2.objects.get(request_id=id).delete()
        return Response({'response': 'This response from delete method'})
    
    

