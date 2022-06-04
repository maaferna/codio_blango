from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail, UserDetail
from rest_framework.authtoken import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os

schema_view = get_schema_view(openapi.Info(
    title="Blango API",
    default_version="v1",
    description="API for Blango Blog",),
    url=r"http://127.0.0.1:8000/api/v1/",public=True,)

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(),name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("users/<str:email>", UserDetail.as_view(),name="api_user_detail"),
    re_path(r"^swagger(\.json|\.yaml)$",schema_view.without_ui(cache_timeout=0),name="schema-json",),
    path("swagger/",schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui",),
]    
urlpatterns = format_suffix_patterns(urlpatterns)


