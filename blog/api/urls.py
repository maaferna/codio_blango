from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from blog.api.views import PostList, PostDetail, UserDetail, TagViewSet, PostViewSet

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os


schema_view = get_schema_view(openapi.Info(
    title="Blango API",
    default_version="v1",
    description="API for Blango Blog",),
    url=r"http://127.0.0.1:8000/api/v1/",public=True,)

urlpatterns = [path("users/<str:email>", UserDetail.as_view(),name="api_user_detail"),]

router = DefaultRouter()
router.register(r"tags", TagViewSet)
router.register(r"posts", PostViewSet)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(),name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$",schema_view.without_ui(cache_timeout=0),name="schema-json",),
    path("swagger/",schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui",),
    path("", include(router.urls)),
    path("posts/by-time/<str:period_name>/",PostViewSet.as_view({"get": "list"}),name="posts-by-time",),
]



