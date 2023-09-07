from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, CommentViewSet, PostViewSet


api_v1 = SimpleRouter()
api_v1.register('posts', PostViewSet, basename='posts')
api_v1.register('groups', GroupViewSet, basename='group')
api_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include(api_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
