
from django.contrib import admin
from django.urls import path, include
from testapp import views
from testapp.views import SegmentcliApiList
from testapp.models import CR_TABLE
from testapp.resources import CRIdResource

#from django.conf.urls import url, include
note_resource = CRIdResource()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.SegmentcliApiList.as_view()),
    path('api/', include(note_resource.urls)),
]



#from django.urls import path, include
#from django.contrib import admin
#from api.resources import NoteResource
#
#note_resource = NoteResource()
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('api/', include(note_resource.urls)),
#]
