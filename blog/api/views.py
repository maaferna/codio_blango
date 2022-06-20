from crypt import methods
from multiprocessing import context
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, TagSerializer
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blog.models import Post, Tag
from blango_auth.models import User

from django.utils.decorators import method_decorator
from django.utils import timezone
from django.db.models import Q 

from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly| IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(cache_page(300))
    def get(self, *args, **kwargs):
        return super(UserDetail, self).get(*args, **kwargs)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(tag.posts, many=True, context={"request":request})
        return Response(post_serializer.data)

    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer
    
    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(vary_on_cookie)
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.queryset().filter(author=request.user)
        serializer = PostSerializer(posts, many=True, context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):            
        if self.request.user.is_anonymous:
            #published only
            return self.queryset.filter(published_at__lte=timezone.now())
        
        if not self.request.user.is_staff:
            #allow all
            return self.queryset
        
        #filter for own or
        return self.queryset.filter(Q(published_at__lte=timezone.now())| Q(author=self.request.user))
    
    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)


