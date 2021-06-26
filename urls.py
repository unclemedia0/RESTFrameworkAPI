from django.urls import path, include
from .views import *

urlpatterns = [
	# localhost:8000/alltask

    path('alltask/', api_alltask),
    path('api-task/', api_get_alltask),
    path('api/<int:pk>/', api_get_alltask_id),
    path('api-post', api_post_alltask), #ไม่ต้องใส่ / ด้าน url
    path('<int:pk>/api-edit', api_put_alltask),
    path('<int:pk>/delete', api_delete_alltask),
    #url('MYAPP', views.index),

]



