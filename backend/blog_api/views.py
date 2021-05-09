from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    # only author of the post can edit it
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # SAFE_METHODS - GET, OPTIONS, HEAD
            return True
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    # permission classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    # postobjects - flagged as 'published'
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
