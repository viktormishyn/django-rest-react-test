from rest_framework import routers
from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

# ================================== APIView based views =====================================

# from django.urls import path
# from .views import PostList, PostDetail

# app_name = 'blog_api'

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate')
# ]
