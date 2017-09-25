from rest_framework.generics import ListAPIView

from .serializers import PostSerializer, CommentSerializer
from .models import  Post, Comment

class PostApi(ListAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer

class CommentApi(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
