from django.shortcuts import render
from rest_framework import viewsets, views, mixins
from django import views
from Crawler.serializers import *


class ConfigViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
