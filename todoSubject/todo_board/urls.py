from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_board'

urlpatterns = [
    url(r'^$', views.Todo_board.as_view(), name='todo_board'),
    url(r'^insert/$', views.check_post, name='todo_board_insert'),
    url(r'^save_prioirity/$', views.check_post, name='todo_board_save_priority'),
    url(r'^is_complete/$', views.check_post, name='todo_board_is_complete'),
    url(r'^is_non_complete/$', views.check_post, name='todo_board_is_non_complete'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Todo_board_detail.as_view(), name='todo_board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Todo_board_update.as_view(), name='todo_board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Todo_board_delete.as_view(), name='todo_board_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)