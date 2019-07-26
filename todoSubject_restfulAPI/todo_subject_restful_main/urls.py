from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers
app_name = 'todo_subject_restful_main'

#router = routers.DefaultRouter()
#router.register(r'todfo', views.Todo_subject_restful_main)
urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.Todo_subject_restful_main.as_view(), name='todo'),
    url(r'^todo_list/$', views.Todo_subject_restful_main.as_view(), name='todo_list'),
    url(r'^todo_list/create/$', views.Todo_subject_restful_create.as_view(), name='todo_create'),
    url(r'^todo_list/(?P<no>\d+)/$', views.Todo_subject_restful_detail.as_view(), name='todo_detail'),
    url(r'^todo_list/(?P<no>\d+)/update/$', views.Todo_subject_restful_update.as_view(), name='todo_update'),
    url(r'^todo_list/(?P<no>\d+)/delete/$', views.Todo_subject_restful_delete.as_view(), name='todo_delete'),
    #url('list', views.Todo_subject_restful_main.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)