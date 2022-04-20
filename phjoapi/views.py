from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PostSerializer
from photojournal.models import Post, Comments


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/v1/posts'},
        {'GET': '/api/v1/posts/id'},
        {'POST': '/api/v1/posts/id/comment'},

        {'POST': '/api/v1/users/token'},
        {'POST': '/api/v1/users/token/refresh'},
        {'POST': '/api/v1/users/token/verify'},

    ]
    return Response(routes)


@api_view(['GET'])
def get_posts(request):
    projects = Post.objects.all()
    serializer = PostSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, pk):
    project = Post.objects.get(id=pk)
    serializer = PostSerializer(project, many=False)
    return Response(serializer.data)
