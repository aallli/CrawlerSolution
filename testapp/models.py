from django.db import models


class CRId(models.Model):
#    movie_id = models.IntegerField()
    
    resource = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    res_ID = models.CharField(max_length=200)
    
#    resource_name = 'crid'

    
class CR_TABLE(models.Model):
#    movie_id = models.IntegerField()
    
    resource = models.CharField(max_length=1000)
    res_ID = models.IntegerField()
    
    resource_name = 'resource'
    

class CRId2(models.Model):
#    movie_id = models.IntegerField()
    request_id = models.AutoField(primary_key = True)
    keyword = models.CharField(max_length=200)
#    platform = models.CharField(max_length=200)
    res_ID = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
#    resource_name = 'crid'