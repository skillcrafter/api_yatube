from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, CommentViewSet, PostViewSet


api_v1 = SimpleRouter()
api_v1.register('v1/posts', PostViewSet, basename='posts')
api_v1.register('v1/groups', GroupViewSet, basename='group')
api_v1.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('', include(api_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
